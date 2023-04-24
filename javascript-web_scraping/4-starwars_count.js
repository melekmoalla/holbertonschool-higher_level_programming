#!/usr/bin/node

const movie = process.argv[2];

const request = require('request');

const m = movie.slice(0, 30);
const movietru = m + 'people/18';
request(movietru, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie5 = JSON.parse(body);
    const len = movie5.films;
    console.log(len.length);
  }
});
