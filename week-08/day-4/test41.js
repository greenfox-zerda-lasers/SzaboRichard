'use strict';
var test = require('tape').test;
var add = require('./41');
test('if funciton works with normal', function(t) {
  let actual = add([3,4,3]);
  let expected = 10;
  t.equal(actual, expected);
  t.end();
});

test('if funciton works with empty list', function(t) {
  let actual = add([]);
  let expected = 0;
  t.equal(actual, expected);
  t.end();
});

test('if funciton works with string', function(t) {
  let actual = add('string');
  let expected = 0;
  t.equal(actual, expected);
  t.end();
});
