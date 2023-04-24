#!/usr/bin/node

const movie = process.argv[2];

const request = require('request');
const m1 = movie.split('/');
const m = `https://${m1[2]}/api/people/18/`;
request(movie, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie5 = JSON.parse(body).results;
    let coun = 0;
    for (let i = 0; i < movie5.length; i++) {
      const p = movie5[i].characters;
      if (p.includes(m)) {
        coun++;
      }
    }
    console.log(coun);
  }
});
