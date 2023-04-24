#!/usr/bin/node

const movie = process.argv[2];

const request = require('request');

request(movie, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie5 = JSON.parse(body).results;
    let coun = 0;
    for (let i = 0; i < movie5.length; i++) {
      const p = movie5[i].characters;
      if (p.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        coun++;
      }
    }
    console.log(coun);
  }
});
