#!/usr/bin/node
const movie = process.argv[2];
const file = process.argv[3];
const fs = require('fs');
const request = require('request');

request(movie, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(file, body, err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
