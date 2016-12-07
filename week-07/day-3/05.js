'use strict';

var numbers = [2.4, 3.5, 1.7, 3.3, 1.2];

// create a function that takes an array of numbers,
// it should return a new array that consists only the numbers that are
// bigger than 2 and all of it's elements should be rounded

function newReturnedArrayWithRoundedNum(arrayInput) {
   var returnedArry = arrayInput.filter(function(num) {
       return num > 2;
   }).map(function(num) {
       return Math.round(num);
   });
  // arrayInput.forEach(function(number){
  //   if (number > 2) {
  //     returnedArry.push(Math.round(number));
  //   }
  // });

  return returnedArry;

}

console.log(newReturnedArrayWithRoundedNum(numbers));
