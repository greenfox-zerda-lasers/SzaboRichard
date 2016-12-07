'use strict';

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

function Student(studGrade) {
  this.grade = studGrade;
  this.grades = []
  this.addgrade = function(grade) {
    if (grade >= 1 && grade <= 5) {
      this.grades.push(grade);
    }
  }
  this.getAverage = function(studGrade) {
    var sum = 0;
    this.grades.forEach(function(elem) {
      sum += elem;
    });
    return sum / this.grades.length;
   }
}

var stundent = new Student();
stundent.addgrade(1);
stundent.addgrade(5);
stundent.addgrade(4);
stundent.addgrade(2);
console.log(stundent.getAverage());
