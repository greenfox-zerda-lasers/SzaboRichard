'use strict';

const http = require('http');


// let date = Date.now();
const server = http.createServer(function serverListen(req, res) {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('The request come from: ' + req.url + '\nHey! Fuuuu: ' + new Date().toISOString());
});

server.listen(3000, '127.0.0.1');
