'use strict';
let button = document.querySelector('button');

load();
function load() {
// (function load() {
  let xhr = new XMLHttpRequest();
  let url = 'https://mysterious-dusk-8248.herokuapp.com/todos';
  xhr.open('GET', url, true);
  xhr.send();
  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      init(JSON.parse(xhr.response));
      console.log(xhr.response);
    }
  }
};
// })();


function init(todoData) {
  let tdDiv = document.querySelector('.todo-item');
  tdDiv.innerHTML = "";
  todoData.forEach(function(item, index){
    let tdWraper = document.createElement('section');
    let binCheckDiv = document.createElement('div');
    let label = document.createElement('label');
    let deleteTD = document.createElement('button');
    let checkTD = document.createElement('div');
    binCheckDiv.className = "inner-separator";
    tdWraper.className = "todo-item-wrapper";
    label.textContent = item.text;
    label.className = "label-for-todo";
    deleteTD.dataset.index = item.id;
    deleteTD.className = "trashbin";
    checkTD.className = "alter-checkbox";
    checkTD.dataset.index = item.id;
    checkTD.addEventListener('click', function(){
      changeIMG(checkTD);
      upDateCheck(this);
  });
    deleteTD.addEventListener('click', function(){
      deleteToDo(this.dataset.index);
      tdWraper.innerHTML = "";
    })
    tdDiv.appendChild(tdWraper);
    tdWraper.appendChild(label);
    tdWraper.appendChild(binCheckDiv);
    binCheckDiv.appendChild(deleteTD);
    binCheckDiv.appendChild(checkTD);

  })
};

function addToDoo() {
  let xhr = new XMLHttpRequest();
  let url = 'https://mysterious-dusk-8248.herokuapp.com/todos';
  xhr.open('POST', url, true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(getData());
  load();
}

function getData() {
  var returnedToDo = {};
  returnedToDo.text = document.querySelector('input[name=todo]').value;
  document.querySelector('input[name=todo]').value = "";
  // returnedToDo = document.querySelector('alter-checkbox');
  // console.log(returnedToDo);
  return JSON.stringify(returnedToDo);
}

button.addEventListener('click', addToDoo);

function deleteToDo(index) {
  let xhr = new XMLHttpRequest();
  let url = 'https://mysterious-dusk-8248.herokuapp.com/todos/'+index;
  xhr.open('DELETE', url, true);
  xhr.setRequestHeader('Accept', 'application/json');
  xhr.send();

}

function upDateCheck(item) {
  let returnedToDo = {};
  let xhr = new XMLHttpRequest();
  let url = 'https://mysterious-dusk-8248.herokuapp.com/todos/'+item.dataset.index;
  xhr.open('PUT', url, true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      checkedChekcer(JSON.parse(xhr.response));
      // console.log(xhr.response);
    }
  }
  xhr.send(checkedChekcer());
}

function checkedChekcer(item) {
  let obj = {};
  obj.text = item.parentNode.parentNode.querySelector('label').textContent;
  if (item.completed === false) {
    obj.completed = true;
    // obj.text = item.text;
  } else {
    obj.completed = false;
    // obj.text = item.text;
  }
  return JSON.stringify(obj);
}

function changeIMG(item){
  item.classList.toggle("alter-checkbox-checked")
  item.parentElement.parentElement.children[0].classList.toggle("label-for-todo-o");
  // console.log("!!!!!!!" +item);
  // console.log(item.parentElement.parentElement.children[0]);
}

// function createToDo() {}

// createToDo();
