'use strict';


// create a function that takes a string and a letter and returns a boolean
// it should return true if the string consits the given letter, false otherwise

function letterInWord(word, letter) {
  return word.split('').some(function(char) {
    return letter === char;
  });
}

console.log(letterInWord("pear", "a"));
