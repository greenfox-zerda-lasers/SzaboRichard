var myUlList = document.querySelector('.asteroids');
// var removeKing = document.querySelector('.asteroids li');

var rem = myUlList.removeChild(document.querySelector('.asteroids li'));
// console.log(rem);

// for ( var i = 0; i < 3; i++ ) {
//   var fox = document.createElement('li');
//   fox.textContent = 'The Fox';
//   myUlList.appendChild(fox);
// };

function foxCreator() {
  var fox = document.createElement('li');
  fox.textContent = 'The Fox';
  return fox;
}
for (var i = 0; i < 3; i++) {
  myUlList.appendChild(foxCreator());
}
