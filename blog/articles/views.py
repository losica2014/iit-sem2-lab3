from articles.models import Article
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import Http404

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    if not request.user.is_anonymous:
        if request.method == 'POST':
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            if form["text"] and form["title"]:
                if Article.objects.filter(title=form["title"]).count() > 0:
                    form['errors'] = "Статья с таким названием уже существует"
                    return render(request, 'create_post.html', {'form': form})
                else:
                    article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                    return redirect('get_article', article_id=article.id)
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})

    else:
        raise Http404

def register(request):
    if not request.user.is_anonymous:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = {
                'username': request.POST["username"],
                'email': request.POST["email"],
                'password': request.POST["password"]
            }
            if form["username"] and form["email"] and form["password"]:
                if User.objects.filter(email=form["email"]).count() > 0:
                    form['errors'] = "Пользователь с таким email уже существует"
                    return render(request, 'register.html', {'form': form})
                elif User.objects.filter(username=form["username"]).count() > 0:
                    form['errors'] = "Пользователь с таким именем уже существует"
                    return render(request, 'register.html', {'form': form})
                else:
                    user = User.objects.create_user(username=form["username"], email=form["email"], password=form["password"])
                    login(request, user)
                    return redirect('/')
            else:
                form['errors'] = "Не все поля заполнены"
                return render(request, 'register.html', {'form': form})
        else:
            return render(request, 'register.html')

def login_view(request):
    if not request.user.is_anonymous:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = {
                'username': request.POST["username"],
                'password': request.POST["password"]
            }
            if form["username"] and form["password"]:
                user = authenticate(request, username=form["username"], password=form["password"])
                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    form['errors'] = "Неверный логин или пароль"
                    return render(request, 'login.html', {'form': form})
            else:
                form['errors'] = "Не все поля заполнены"
                return render(request, 'register.html', {'form': form})
        else:
            return render(request, 'login.html')

def logout_view(request):
    if not request.user.is_anonymous:
        logout(request)
    return redirect('/')