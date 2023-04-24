#!/usr/bin/node

const file = process.argv[2];
const content = process.argv[3];
const fs = require('fs');

fs.writeFile(file, content, err => {
  if (err) {
    console.error(err);
  }
});
