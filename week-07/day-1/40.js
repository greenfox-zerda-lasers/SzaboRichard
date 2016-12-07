'use strict'

var aj = 'kuty'
// write a function that gets a string as an input
// and appends an 'a' character to its end and returns a new string
function aAppender(string) {
  if (typeof string === "string") {
    var returnedString = ""
    returnedString = string +"a";
    return returnedString;
  }
  else {
    console.log("Basic error handling!");
  }
}

console.log(aAppender(aj));
