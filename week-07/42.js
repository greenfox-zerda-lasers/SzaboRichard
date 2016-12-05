'use strict';
// create a function that returns it's input factorial

function returnMyFactorial (num) {
  for (var answer = 1; num > 0; num--) {
    answer*= num;
  }
  return answer;
}

console.log(returnMyFactorial(3));
