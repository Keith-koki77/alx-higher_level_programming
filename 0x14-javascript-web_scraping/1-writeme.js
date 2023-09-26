#!/usr/bin/node
// Script that writes a string to a file.

const fs = require('fs');
const file = process.argv[2];
const content = process.argv[3];

// Write the string to the file asynchronously with utf-8 encoding
fs.writeFile(file, content, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
