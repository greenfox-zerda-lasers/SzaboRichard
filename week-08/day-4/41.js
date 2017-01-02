'use strict';

var numbers = [4, 5, 6, 7, 8, 9, 10]
// write your own sum function

module.exports = function(num) {
  if ( Array.isArray(num) ) {
    let sum = 0;
    num.forEach( function(val) {
      return sum += val;
    });
    return sum;
  }
  else {
    return 0;
  }
};
