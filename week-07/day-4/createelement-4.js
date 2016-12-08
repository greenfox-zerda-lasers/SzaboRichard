var myList = document.querySelector('.asteroids');
var removedKing = myList.removeChild(document.querySelector('.asteroids li'));

planetData.forEach(function(value){
  if (value.asteroid) {
     var newLi = document.createElement('li');
     newLi.classList.add(value.category);
     newLi.textContent = value.content;
     myList.appendChild(newLi);
  }
  // console.log(value);
});
