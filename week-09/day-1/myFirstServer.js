'use strict';

var express = require('express');

var exampleApp = express();

exampleApp.get('/', function getApp(req, res) {
  res.send('Am I alive?');
});

exampleApp.post('/', function getApp(req, res) {
  res.send('post this shit');
});

exampleApp.listen(3000);
