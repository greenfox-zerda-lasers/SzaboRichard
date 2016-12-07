
'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1, e: 1}

var apple = "apple";

function wordCounterInWordWithItSChars (word) {
  return word.split('').reduce(function(allChars, char) {
    if (char in allChars) {
      allChars[char]++;
    } else {
      allChars[char] = 1;
    }
    return allChars;
  }, {});
}

console.log(wordCounterInWordWithItSChars(apple));
