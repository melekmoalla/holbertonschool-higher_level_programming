#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    return;
  }

  const films = JSON.parse(body).results;
  let count = 0;

  films.forEach((film) => {
    const characters = film.characters;
    if (characters.includes(`https://swapi.dev/api/people/${characterId}/`)) {
      count++;
    }
  });

  console.log(count);
});
