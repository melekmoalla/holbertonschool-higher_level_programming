#!/usr/bin/node

const num = process.argv;
if (num[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num[2]; i++) {
    console.log('C is fun');
  }
}
