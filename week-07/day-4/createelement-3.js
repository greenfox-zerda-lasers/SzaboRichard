var removedItem = document.querySelector('.asteroids').removeChild(document.querySelector('.asteroids li'));
console.log(removedItem);

function listItemTextAdderCreator(array) {
  for (var i = 0; i < array.length; i++) {
    var newLiItem = document.createElement('li')
    newLiItem.textContent = array[i];
    document.querySelector('.asteroids').appendChild(newLiItem);
  };
  return newLiItem;
}

var textArray = ['apple', 'bubble', 'cat', 'green fox'];
listItemTextAdderCreator(textArray);
