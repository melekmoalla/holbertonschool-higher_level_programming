#!/usr/bin/node

const request = require('request');

const number_id = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${number_id}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
