#!/usr/bin/node
const a = process.argv;
let p = 0;
let m = 0;
for (let i = 2; i < a.length; i++) {
  if (p < parseInt(a[i])) {
    m = p;
    p = a[i];
    console.log(m);
  }
}
console.log(m);
