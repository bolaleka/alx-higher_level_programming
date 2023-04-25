#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

request(`https://swapi.dev/api/films/${movieId}/`, function (error, response, body) {
  if (error) throw error;

  const charactersUrls = JSON.parse(body).characters;

  const getCharacterName = (url) => {
    return new Promise((resolve, reject) => {
      request(url, function (error, response, body) {
        if (error) reject(error);
        resolve(JSON.parse(body).name);
      });
    });
  };

  Promise.all(charactersUrls.map(getCharacterName))
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(error => {
      throw error;
    });
});
