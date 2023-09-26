#!/usr/bin/node
// Script that display the status code of a GET request.

const request = require('request');

if (process.argv.length > 2) {
  request(process.argv[2], (err, res, body) => {
    if (err) console.log(err);
    console.log('code:', res.statusCode);
  });
}
