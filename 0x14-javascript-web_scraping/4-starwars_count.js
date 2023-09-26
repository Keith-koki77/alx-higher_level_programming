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
    console.log(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error:', `Status Code ${response.statusCode}`);
    process.exit(1);
  }

  const filmsData = JSON.parse(body);
 
  const wedgeAntillesFilms = filmsData.results.filter((film) =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
  );

  console.log(wedgeAntillesFilms.length);
});
