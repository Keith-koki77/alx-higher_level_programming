#!/usr/bin/node
//Script that gets the contents of a webpage and stores it in a file

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
