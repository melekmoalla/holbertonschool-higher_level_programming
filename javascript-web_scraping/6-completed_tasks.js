#!/usr/bin/node
const movie = process.argv[2];
const request = require('request');

request(movie, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const li = {};
    const m = JSON.parse(body);
    for (let i = 0; i < m.length; i++) {
      if (m[i].completed === true) {
        if (isNaN(li[m[i].userId])) {
          li[m[i].userId] = 0;
        }
        li[m[i].userId]++;
      }
    }
    console.log(li);
  }
});
