'use strict'

var aj = 'kuty'
// write a function that gets a string as an input
// and appends an 'a' character to its end and returns a new string

module.exports = function(string) {
  if ( typeof string === "string") {
    return string+'a';
  } else {
    return ('not a string');
  }
}
