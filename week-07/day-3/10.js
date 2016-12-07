'use strict';

// create a student object
// that has a method `addGrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

function Student(studGrade) {
  this.grade = studGrade;
  this.grades = [];
  this.addGrade = function(grade) {
    if (grade >= 1 && grade <= 5) {
      this.grades.push(grade);
    }
  };
  this.addGrades = function(gradeArray) {
    gradeArray.forEach(function(elem) {
      this.addGrade(elem);
    }, this);
  };
  this.getAverage = function(studGrade) {
    var sum = 0;
    this.grades.forEach(function(elem) {
      sum += elem;
    });
    return sum / this.grades.length;
  };
}

var stundent = new Student();
stundent.addGrade(1);
stundent.addGrades([1,4,3,1,1,4,1,5]);
stundent.addGrade(5);
stundent.addGrade(4);
stundent.addGrade(2);
console.log(stundent.getAverage());
