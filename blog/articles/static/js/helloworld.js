var students = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "group": "БВТ1702",
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "group": "БСТ1702",
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "group": "БАП1801",
        "marks": [5, 5, 5]
    }
];


function printStudents(s) {
    console.table(s);
}

function mean(numbers) {
    r = 0;
    for(var i = 0; i < numbers.length; i++) r += numbers[i];
    return r / numbers.length;
}

function filterStudentsByMeanMark() {
    mark = prompt("Введите балл:")
    filtered = []
    for (var i = 0; i < students.length; i++) {
        s = students[i]
        if(mean(s['marks']) >= mark) filtered.push(s);
    }
    printStudents(filtered)
}

function filterStudentsByGroup() {
    group = prompt("Пожалуйста, введите группу:")
    filtered = []
    for (var i = 0; i < students.length; i++) {
        s = students[i]
        if(s['group'] == group) filtered.push(s);
    }
    printStudents(filtered)
}
