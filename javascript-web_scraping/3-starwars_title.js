#!/usr/bin/node

const request = require('request');
const n = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${n}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
