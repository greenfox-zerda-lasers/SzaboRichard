var test = require('tape').test;
var add = require('./39');
test('if function double its input', function (t) {
  var actual = add(2);
  var expected = 4;
  t.equal(actual, expected);
  t.end();
});

test('if function double its float input', function (t) {
  var actual = add(2.5);
  var expected = 5;
  t.equal(actual, expected);
  t.end();
});

test('if function double its string input', function (t) {
  var actual = add("yo");
  var expected = ('Not a number!'); //isnone
  t.equal(actual, expected);
  t.end();
});
