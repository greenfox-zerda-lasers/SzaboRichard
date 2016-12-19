'use strict';
let button = document.querySelector('.addThis');

load();
function load() {
// (function load() {
  let xhr = new XMLHttpRequest();
  let url = 'https://mysterious-dusk-8248.herokuapp.com/todos';
  xhr.open('GET', url, true);
  xhr.send();
  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      init(JSON.parse(xhr.response).reverse());
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
    if (item.completed === true) {
      checkTD.className = "alter-checkbox-checked";
    } else {
      checkTD.className = "alter-checkbox";
    }
    binCheckDiv.className = "inner-separator";
    tdWraper.className = "todo-item-wrapper";
    label.textContent = item.text;
    label.className = "label-for-todo";
    deleteTD.dataset.index = item.id;
    deleteTD.className = "trashbin";
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
  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      load();
    }
  }
  xhr.send(getData());
}

function getData() {
  var returnedToDo = {};
  returnedToDo.text = document.querySelector('input[name=todo]').value;
  document.querySelector('input[name=todo]').value = "";
  // returnedToDo = document.querySelector('alter-checkbox');
  // console.log(returnedToDo);
  return JSON.stringify(returnedToDo);
}

button.addEventListener('click',  function(){
  load();
  addToDoo();
});

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
  let returnedData = checkedChekcer(item);
  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      console.log(xhr.response);
    }
  }
  console.log(returnedData);
  xhr.send(returnedData);
}

function checkedChekcer(item) {
  let obj = {};
  obj.text = item.parentNode.parentNode.querySelector('label').textContent;
  if (item.classList.contains("alter-checkbox-checked")) {
    obj.completed = true;
    console.log(obj.text);
  } else {
    obj.completed = false;
  }
  console.log(obj.text);
  return JSON.stringify(obj)
}

function changeIMG(item){
  // console.log("chg item: "+item);
  item.classList.toggle("alter-checkbox-checked")
  item.parentElement.parentElement.children[0].classList.toggle("label-for-todo-o");
}

let musicB = document.querySelector('.music');
var music = document.querySelector('audio');
var allowedKeys = {
  37: 'left',
  38: 'up',
  39: 'right',
  40: 'down',
  65: 'a',
  66: 'b'
};
var konamiCodePosition = 0;
var konamiCode = ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right', 'b', 'a'];

document.addEventListener('keyup', function(e){
  var key = allowedKeys[e.keyCode];
  var requiredKey = konamiCode[konamiCodePosition];

  if (key == requiredKey) { //in arrayre átírni
    konamiCodePosition++;
    if (konamiCodePosition === konamiCode.length) {
      music.classList.toggle('audio-on');
      window.alert("Empire Strikes Back");
    }
  } else {
    konamiCodePosition = 0;
  }

})
