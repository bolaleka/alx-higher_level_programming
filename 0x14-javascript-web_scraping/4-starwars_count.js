#!/usr/bin/node

// prints the number of movies where the character is present
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body).results;
  const numFilmsWithWedge = films.filter(film => {
    return film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/');
  }).length;

  console.log(numFilmsWithWedge);
});
