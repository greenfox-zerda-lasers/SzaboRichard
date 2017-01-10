'use strict';

var express = require('express');
var app = express();
var bodyParser = require('body-parser')
var mysql = require('mysql');
var decoder = require('./decode');

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use('/', express.static('../public'));

var connection = mysql.createConnection({
  host     : 'localhost',
  user     : "'root'",
  password : 'admin',
  database : 'caesar'
});

connection.connect();

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

app.get('/decode/all', function (req, res) {
  connection.query('SELECT * FROM decript', function(err, rows, fields){
    if (!err) {
      var rowsTextOnly = rows.map( function (row){
        return row.text;
      });
      res.send({
        all: rowsTextOnly
      });
    } else {
      console.log(err);
    }
  })
});

app.post('/decode/', function decode (req, res) {
  console.log(req.body.text, req.body.shift);
  connection.query({
  		sql: 'INSERT INTO decript(shift, text) VALUES(?, ?)',
  		values: [ req.param.shift, decoder( req.body.shift, req.body.text)]
  	}, function(err, rows, fields) {
  		if (err) {
        throw err;
      } else {
        res.send(rows);
      }
    });
});

app.listen(3600, function(){
	console.log('SERVER IS UP AND RUNNIN on port: 3600')
});