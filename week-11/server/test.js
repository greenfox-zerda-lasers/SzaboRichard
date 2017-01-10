'use strict';
var test = require('tape');
var decrypt = require('./decode.js');

test('true', function (t) {
  t.equal(1, 1);
  t.end();
});

test('decrypt rome with 0', function (t) {
  t.equal(decrypt(0, 'For Rome'), 'For Rome');
  t.end();
})

test('decrypt lorem ipsum with 3', function (t) {
  t.equal(decrypt(1, 'oruhp lsvxp groru vlw'), 'psviq mtwyq hspsv wmx');
  t.end();
})

test('decrypt lorem ipsum with 25', function (t) {
  t.equal(decrypt(-3, 'oruhp lsvxp groru vlw'), 'psviq mtwyq hspsv wmx');
  t.end();
})
