#!/usr/bin/node
// Script that prints the title of a Star Wars movie where
// the episode number matches a given integer

const request = require('request');

// Check if a movie ID argument is provided
if (process.argv.length < 3) {
  console.error('Please provide a movie ID as the first argument.');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

const data = JSON.parse(body);

if (data && data.title) {
  console.log(`${data.title}`);
} else {
  console.error('Movie not found or title not available.');
}
});
