'use strict';
let button = document.querySelector('button');

(function load() {
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
})();

function init(todoData) {
  todoData.forEach(function(item, index){
    let tdDiv = document.querySelector('.todo-item');
    let tdWraper = document.createElement('section');
    let binCheckDiv = document.createElement('div');
    let label = document.createElement('label');
    let deleteTD = document.createElement('button');
    let checkTD = document.createElement('div');
    binCheckDiv.className = "inner-separator";
    tdWraper.className = "todo-item-wrapper";
    label.textContent = item.text;
    label.className = "label-for-todo";
    deleteTD.className = "trashbin";
    checkTD.className = "alter-checkbox";
    // checkTD.addEventListener('click', function(e){
    //   let cheecked = false;
          // if (checked === false) {
          //   checked = !checked;
          // } else {
          //   checked = !checked;
          // }
    // });
    // deleteTD.addEventListener('click', function(){
    //   deleteToDo();
    // };)
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

}

function getData() {
  var returnedToDo = {};
  returnedToDo.text = document.querySelector('input[name=todo]').value;
  // returnedToDo = document.querySelector('alter-checkbox');
  // console.log(returnedToDo);
  return JSON.stringify(returnedToDo);
}

button.addEventListener('click', addToDoo);

// function checkfunction(){
//   let trueOrFalse = false;
//
// }

// function createToDo() {}

// createToDo();
