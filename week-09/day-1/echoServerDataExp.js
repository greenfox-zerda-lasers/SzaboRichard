'use strict';

var express = require('express');

var exampleApp = express();

exampleApp.get('/', function getApp(req, res) {
  res.send('Hi there Mr. ' + req.url + '\nThe requested time is: ' + new Date().toString());
});

exampleApp.listen(3000);
