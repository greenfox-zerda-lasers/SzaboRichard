'use strict';
var toDo = ['Wake up', 'Learn JS']
// function toDoData(obj) {
//   console.log(obj);
// }

function createToDo() {
  toDo.forEach(function(item){
    let tdDiv = document.querySelector('.todo-item');
    let label = document.createElement('label');
    let deleteTD = document.createElement('button');
    let checkTD = document.createElement('div');
    label.textContent = item;
    label.className = "label-for-todo";
    deleteTD.className = "trashbin";
    checkTD.className = "alter-checkbox";
    tdDiv.appendChild(label);
    tdDiv.appendChild(deleteTD);
    tdDiv.appendChild(checkTD);

  })
}

createToDo();
