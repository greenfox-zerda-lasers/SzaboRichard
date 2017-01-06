'use strict';

var fs = require('fs');
var async = require('async');
var express = require('express');
var bodyParser = require('body-parser');
var meta = require('musicmetadata');
var mysql = require('mysql');
var app = express();

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.use('/', express.static('../public'));

var connection = mysql.createConnection({
      host     : 'localhost',
      user     : "'root'",
      password : 'admin',
      database : 'foxplayer'
});
connection.connect();

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});


app.get('/playlists', function (req, res) {
  connection.query('SELECT * FROM playlists', function(err, rows, fields){
    if (err) {
      throw err;
    } else {
      res.send(rows);
    }
  })
});

// a

app.post("/playlists/", function postPlaylist (req, res) {
  connection.query({
  		sql: 'INSERT INTO playlists(playlist, system) VALUES(?, ?)',
  		values: ['Hello', 0]
  	}, function(err, rows, fields) {
  		if (err) throw err;
      // console.log(rows);
      // rows = rows.map(rows);
    	res.send(rows);
    });
});



app.delete("/playlists/:id", function deletePlaylist (req, res) {
  connection.query('DELETE FROM playlists WHERE id = \'' + req.params.id + '\'', function(err, rows){
    if (err) {
      console.log(err.toString());
    }
    res.send(rows);
  });

});


app.get('/playlist-tracks/', function (req, res) {
  connection.query('SELECT * FROM tracks', function(err, rows){
    if (err) {
      throw err;
    }
    res.send(rows);
  });
});


app.get("/playlist-tracks/:track_id", function getPlaylist (req, res) {
  connection.query('SELECT * FROM tracks WHERE playlist_id = \'' + req.params.id + '\'', function(err, rows){
    if (err) {
      throw err;
    }
    res.send(rows);
  });
});

app.post("/playlist-tracks/:playlist_id", function postPlaylist (req, res) {
  connection.query({
    sql : 'INSERT INTO tracks(path, playlist_id) VALUES(?,?)',
    values : ['test', req.params.playlist_id]
  }, function(err, rows){
    if (err) {
      throw err;
    }
    res.send(rows);
  });
});

app.delete("/playlist-tracks/:playlist_id/:track_id", function deletePlaylist (req, res) {
  connection.query({
    sql : 'DELETE FROM tracks WHERE playlist_id = ? AND id = ?' ,
    values : [req.params.playlist_id, req.params.track_id]
    }, function(err, rows){
    if (err) {
      throw err;
    }
    res.send(rows);
  });
});

app.get('/tracks', function(req, res) {
	fs.readdir('../public/tracks/', function (err, files) {
		var coll = [];
		async.each(
			files,
			function (file, callback){
				meta(fs.createReadStream('../public/tracks/' + file), function (err, metadata) {
					metadata.fileName = file;
					coll.push(metadata);
				 	callback();
				});
			},
			function(){
  				res.send(coll);
			}
		);
	});
});



module.exports = app;

app.listen(3000, function(){
	console.log('SERVER IS UP AND RUNNIN on port: 3000')
});
