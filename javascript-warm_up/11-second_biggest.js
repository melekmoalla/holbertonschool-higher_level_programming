#!/usr/bin/node
const a = process.argv[2];

if (isNaN(a) || a === 1) {
  console.log(0);
} else {
  console.log(a);
}
