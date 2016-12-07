'use strict';

var numbers = [3, 4, 5, 6, 7];
// write a function that filters the odd numbers
// from an array and returns a new array consisting
// only the evens
function arrayFilter(arrayInput) {
  var returnArray = []
  for (var i = 0; i < arrayInput.length; i++) {
    if (arrayInput[i] % 2 === 1) {
      returnArray.push(arrayInput[i]);
    }
  }
  return returnArray
}

console.log(arrayFilter(numbers));
