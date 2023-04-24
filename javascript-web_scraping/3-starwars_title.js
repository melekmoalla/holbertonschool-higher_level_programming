#!/usr/bin/node

const request = require('request');
const numberid = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${numberid}`;

request(url, (error, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
