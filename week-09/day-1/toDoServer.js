'use strict';

var express = require('express');

var bodyParser = require('body-parser');

var todoApp = express();

var todoData = require('./motherflippindata');

var userId = todoData.length;

todoApp.use(bodyParser.urlencoded({ extended: false }));
todoApp.use(bodyParser.json());

todoApp.use('/', express.static('./public'));

todoApp.get('/todos', function getAppData(req, res) {
  res.send(JSON.stringify(todoData));
});

todoApp.get('/todos/:id', function getAppDataId(req, res) {
  res.send('The listed data by id: ' + JSON.stringify(todoData[parseInt(req.params.id)]));
});


todoApp.post('/todos/', function postAppData(req, res) {
  var userText = req.body.text;
  var completed = false;
  userId++;
  var returnedStuff =
    {
          "completed": completed,
          "id": userId,
          "text": req.body.text
    };
  todoData.push(returnedStuff);
  res.send(returnedStuff);
});

todoApp.delete('/todos/:id', function deleteAppData(req, res) {
  var deletedItem = todoData.filter(function(item) {
    return item.id != req.params.id;
  });
  todoData = deletedItem;
  res.send(todoData);
});

todoApp.listen(3000);
