#!/usr/bin/node
//Script that reads and prints the content of a file.

const fs = require('fs');

// Get the file path from command line arguments
const file = process.argv[2];

// Read the file asynchronously with utf-8 encoding
fs.readFile(file, 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});

