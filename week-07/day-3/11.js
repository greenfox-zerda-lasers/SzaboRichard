'use strict';

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last element form the stack and also deletes it from it

// please don`t use the built in methods

function Stack(data) {
  this.arrayData = data;
  this.size = function() {
    return this.arrayData.length;
  };
  this.push = function(numberInput) {
    this.arrayData.concat(numberInput);
    return this.arrayData;
  }
  this.pop = function() {
    this.lasteElem = this.arrayData.splice(this.size()-1, 1 );
    return this.lasteElem;
  }
}


var stack = new Stack([1,2,3,4,5,6]);
console.log(stack.size());
console.log(stack.pop());
