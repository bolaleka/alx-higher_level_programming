#!/usr/bin/node
// File: starwars_movie_characters.js

const request = require('request');

const MOVIE_ID = process.argv[2];
const SWAPI_BASE_URL = 'https://swapi.dev/api/';

request(SWAPI_BASE_URL + 'films/' + MOVIE_ID, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const film = JSON.parse(body);
  const charactersUrls = film.characters;
  const characterNames = [];

  function fetchCharacterName (characterUrl) {
    return new Promise((resolve, reject) => {
      request(characterUrl, function (error, response, body) {
        if (error) {
          reject(error);
          return;
        }

        const character = JSON.parse(body);
        characterNames.push(character.name);
        resolve();
      });
    });
  }

  Promise.all(charactersUrls.map(fetchCharacterName))
    .then(() => {
      characterNames.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error(error);
    });
});
