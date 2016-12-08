var myList = document.querySelector('.asteroids');
var removedKing = myList.removeChild(document.querySelector('.asteroids li'));

planetData.forEach(function(value){
  value.forEach(function(elem) {
    console.log(elem);
  });
  console.log(value);
});
