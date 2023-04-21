#!/usr/bin/node

const dict = require('./101-data').dict;

const Dict = {};

for (const userId in dict) {
  const occurrence = dict[userId];

  if (!Dict[occurrence]) {
    Dict[occurrence] = [];
  }

  Dict[occurrence].push(userId.toString());
}

console.log(Dict);
