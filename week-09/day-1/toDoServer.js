'use strict';

var express = require('express');

var bodyParser = require('body-parser');

var todoApp = express();

// var todoData = require('./motherflippindata');

var mysql = require('mysql');

var con = mysql.createConnection({
  host: 'localhost',
  user: "'root'",
  password: 'admin',
  database: 'todo'
});

// var userId = todoData.length;

todoApp.use(bodyParser.urlencoded({ extended: false }));
todoApp.use(bodyParser.json());

todoApp.use('/', express.static('./public'));

con.connect(function(err){
  if (err) {
    console.log('An erro war given while connected, conn failed!');
    return;
  }
  console.log('Connection RDY');
});


todoApp.get('/todos', function getAppData(req, res) {
  con.query('SELECT *\
            FROM todo;', function(err, rows){
              if (err) {
                console.log(err.toString());
                return;
              }
              rows = rows.map(function(el){
                el.completed = (el.completed) ? true : false;
                return el;
              })
              res.send(JSON.stringify(rows)
              );
            })
});


todoApp.post('/todos/', function postAppData(req, res) {
  con.query('INSERT INTO todo(text, completed) VALUES (\'' + req.body.text + '\', 0)', function(err, rows){
      if (err) {
        console.log(err.toString());
      } else {
        res.send(rows);
      }
   });
});

todoApp.delete('/todos/:id', function deleteAppData(req, res) {
  con.query('DELETE FROM todo WHERE id = \'' + req.params.id + '\'', function(err, rows){
    if (err) {
      console.log(err.toString());
    } else {
      res.send(rows);
    }
  });
});

todoApp.listen(3500);
