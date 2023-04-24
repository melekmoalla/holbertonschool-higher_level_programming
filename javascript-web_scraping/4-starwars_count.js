#!/usr/bin/node
const movie = process.argv[2];
const request = require('request');
let m2;
request(movie, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (movie === 'https://swapi-api.hbtn.io/api/films') {
      m2 = 'https://swapi-api.hbtn.io/api/people/18/';
    } else {
      m2 = 'http://swapi.co/api/people/18/';
    }
    const movie5 = JSON.parse(body).results;
    let coun = 0;
    for (let i = 0; i < movie5.length; i++) {
      const p = movie5[i].characters;
      if (p.includes(m2)) {
        coun++;
      }
    }
    console.log(coun);
  }
});