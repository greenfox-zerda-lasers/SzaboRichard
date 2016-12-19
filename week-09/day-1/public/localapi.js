'use strict';

var express = require('express');

var todoApp = express();

var todoData = require('./motherflippindata')();

todoApp.get('/todos', function getAppData(req, res) {
  res.sendfile(__dirname+'/https://mysterious-dusk-8248.herokuapp.com/todos');
    // JSON.stringify(todoData));
});

todoApp.get('/todos/id', function getAppDataId(req, res) {
  console.log(req.params.id);
  res.send('The listed data by id: ' + req.params.id);
});

todoApp.listen(3000);
