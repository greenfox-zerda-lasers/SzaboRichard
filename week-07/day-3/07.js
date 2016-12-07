'use strict';

var numbers = [2, 5, 11, 29];
var numberZ = [6];

// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise

function isPrime(value) {
    for(var i = 2; i < value; i++) {
        if(value % i === 0) {
            return false;
        }
    }
    return value > 1;
}

function arrayOfTruethIfPrime(array_data) {
  return array_data.every(function(num) {
    return isPrime(num);
  });
}

console.log(arrayOfTruethIfPrime(numbers));
console.log(arrayOfTruethIfPrime(numberZ));
