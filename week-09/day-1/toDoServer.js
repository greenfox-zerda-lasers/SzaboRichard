'use strict';

var express = require('express');

var todoApp = express();

var todoData = require('./motherflippindata')();

todoApp.get('/todos', function getAppData(req, res) {
  res.send('The listed data: ' + JSON.stringify(todoData));
});

todoApp.listen(3000);
