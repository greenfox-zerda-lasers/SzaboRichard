'use strict';

var ai = 123;
// create a function that doubles it's input
// double ai with it

module.exports = function (a) {
  if (a instanceof String) {
    return ('Not a number!');
  } else {
    return 2*a;
  }
};
