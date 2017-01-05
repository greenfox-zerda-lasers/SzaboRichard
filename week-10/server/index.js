'use strict';

var express = require('express');
var mysql = require('mysql');
var app = express();

var connection = mysql.createConnection({
      host     : 'localhost',
      user     : "'root'",
      password : 'admin',
      database : 'foxplayer'
});
connection.connect();

// var playlists = [
//     [{ "id": 21, "title": "Halahula", "artist": "Untitled artist", "duration": 545, "path": "c:/music/halahula.mp3" },
//     { "id": 412, "title": "No sleep till Brooklyn", "artist": "Beastie Boys", "duration": 312.12, "path": "c:/music/beastie boys/No sleep till Brooklyn.mp3" }],
//
//     [{ "id": 33, "title": "Helloo", "artist": "bjdfbje", "duration": 577, "path": "c:/music/helloo.mp3" },
//     { "id": 111, "title": "Brooklyn", "artist": "cats", "duration": 52.12, "path": "c:/music/cats/Brooklyn.mp3" }]
// ];

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



module.exports = app;

app.listen(3000, function(){
	console.log('SERVER IS UP AND RUNNIN on port: 3000')
});
