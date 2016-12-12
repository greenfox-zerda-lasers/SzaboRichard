'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangles(a, b) {
  this.a = a;
  this.b = b;
}

Rectangles.prototype.getArea = function() {
  return this.a*this.b;
}

Rectangles.prototype.getCircumference = function() {
  return 2*(this.a*this.b);
}

var myRect = new Rectangles(5,6);
var notMyRect = new Rectangles(2,3);
console.log(myRect.getArea());
console.log(notMyRect.getArea());
