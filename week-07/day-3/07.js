'use strict';

var numbers = [2, 5, 11, 29];
var numberZ = [1, 5, 11, 29];

// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise

function arrayOfTruethIfPrime(array_data) {
  return array_data.every(function(num) {
    return num % 2 === 1;
  });
}

console.log(arrayOfTruethIfPrime(numbers));
console.log(arrayOfTruethIfPrime(numberZ));
