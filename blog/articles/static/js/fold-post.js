var foldBtns = document.getElementsByClassName("fold-button");
for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function (e) {
        p = e.target.parentElement
        if(p.classList.contains("folded")) {
            p.classList.remove("folded")
            e.target.innerHTML = "свернуть"
        } else {
            p.classList.add("folded")
            e.target.innerHTML = "развернуть"
        }
    });            
}