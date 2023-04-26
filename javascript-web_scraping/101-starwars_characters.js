#!/usr/bin/node
const ar = process.argv[2];
const re = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + ar + '/';
re(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const file = JSON.parse(body).characters;
    for (let i = 0; i < file.length; i++) {
      re(file[i], function (error, response, body) {
        if (error) {
          console.log('Error:', error);
        } else {
          const characterName = JSON.parse(body).name;
          console.log(characterName);
        }
      });
    }
  }
});
