#!/usr/bin/node

const num = process.argv;
let text = '';

if (isNaN(num[2])) {
  console.log('Missing size');
} else {
  for (let o = 0; o < num[2]; o++) {
    text += 'X';
  }
  for (let i = 0; i < num[2]; i++) {
    console.log(text);
  }
}
