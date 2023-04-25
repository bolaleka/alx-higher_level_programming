#!/usr/bin/node

// prints the title of a Star Wars movie from a given integer
const request = require('request');

const movieId = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  } else {
    console.error(`Failed to fetch movie with ID ${movieId}: ${error}`);
    process.exit(1);
  }
});
