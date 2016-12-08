// var button = document.querySelector('button');
//  function alertGreenFox () {
//    alert('Green Fox!');
//  }
//  button.addEventListener('click', alertGreenFox);
var button = document.querySelector('button');
function elemCounter() {
  var list = document.querySelectorAll('li');
  var count = list.length;
   document.querySelector('.result').textContent = count;
}

button.addEventListener('click', elemCounter);
