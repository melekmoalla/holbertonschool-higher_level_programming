#!/usr/bin/node
const movie = process.argv[2];

const request = require('request');
const m1 = movie.split('/');
const m = `${m1[0]}//${m1[2]}/api/people/18`;
request(m, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie5 = JSON.parse(body);
    const len = movie5.films;
    console.log(len.length);
  }
});