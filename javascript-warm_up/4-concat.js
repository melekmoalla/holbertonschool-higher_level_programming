#!/usr/bin/node
const args = process.argv;
let Textt = '';
let a = 1;

for (let i = 2; i <= 3; i++) {
  if (args[i] === undefined) {
    Textt += undefined;
  } else {
    Textt += args[i];
  }
  if (a === 1) {
    a = 2;
    Textt += ' is ';
  }
}
console.log(Textt);
