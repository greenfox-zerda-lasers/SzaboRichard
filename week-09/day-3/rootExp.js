'use strict';

var mysql = require('mysql');

var express = require('express');

var app = express();

var con = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'admin',
  database: 'bookstore'
});

con.connect(function(err){
  if(err) {
    console.log('An error was thrown when you connected FOOL!');
    return;
  }
  console.log('Connection RDY');
});

app.get('/booknames', function(req, res){
  con.query('SELECT book_name\
            FROM book_mast;', function(err, rows){
              if (err) {
                  console.log(err.toString());
                  return;
              }
              res.send(rows);
            });
});

app.get('/books', function(req, res){
  con.query('SELECT book_name, aut_name, cate_descrip, pub_name, book_price\
    FROM book_mast\
    INNER JOIN author\
    ON author.aut_id = book_mast.aut_id\
    INNER JOIN category\
    ON category.cate_id = book_mast.cate_id\
    INNER JOIN newpublisher\
    ON newpublisher.pub_id = book_mast.pub_id;', function(err, rows){
              if (err) {
                  console.log(err.toString());
                  return;
              }
              res.send(rows);
            });
});

app.listen(3000);
