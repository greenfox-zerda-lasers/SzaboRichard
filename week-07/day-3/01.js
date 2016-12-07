'use strict';

// Create a function that takes a number and returns it as string in english
// like 0 -> "zero", it should work with the first 5 numbers, after it should
// return "many"

function numberInEnglish (numberInput) {
  switch (numberInput) {
    case 0:
      return("0 -- > Zero");
      break;
    case 1:
      return("1 --> One");
      break;
    case 2:
      return("2---> Two");
      break;
    case 3:
      return("3 --> Three");
      break;
    case 4:
      return("4 --> Four");
      break;
    case 5:
      return("5 --> Five");
      break;
    default:
      return("MANY");
      break;
  }
}

console.log(numberInEnglish(4));
