#!/usr/bin/node
//Script that prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');

if (process.argv.length < 3) {
  console.log(error);
  process.exit(1);
}

const apiUrl = process.argv[2];
const characterId = 18;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const filmsData = JSON.parse(body);
  
  let wedgeAntillesCount = 0;

  filmsData.results.forEach((film) => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
      wedgeAntillesCount++;
    }

  });

  console.log(`${wedgeAntillesCount}`);
});
