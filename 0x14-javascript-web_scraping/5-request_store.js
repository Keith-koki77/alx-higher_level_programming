#!/usr/bin/node
//Script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');

// Check if the correct number of command-line arguments are provided
if (process.argv.length !== 4) {
  console.error('Usage: node 5-request_store.js <URL> <file_path>');
  process.exit(1);
}

// Get the URL and file path from command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make an HTTP GET request to the specified URL
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Error:', `Status Code ${response.statusCode}`);
    process.exit(1);
  }

  // Write the body of the response to the specified file in UTF-8 encoding
  fs.writeFile(filePath, body, 'utf-8', (writeError) => {
    if (writeError) {
      console.error('Error writing to file:', writeError);
      process.exit(1);
    }

    console.log(`Contents of the webpage ${url} saved to ${filePath}`);
  });
});
