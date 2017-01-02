var test = require('tape').test;
var add = require('./40');
test('if funciton appends a', function(t) {
  let actual = add('kuty');
  let expected = 'kutya';
  t.equal(actual, expected);
  t.end();
});

test('if funciton appends with num', function(t) {
  let actual = add(3);
  let expected = 'not a string';
  t.equal(actual, expected);
  t.end();
});

test('if funciton appends with []', function(t) {
  let actual = add(['sdad','dad']);
  let expected = 'not a string';
  t.equal(actual, expected);
  t.end();
});
