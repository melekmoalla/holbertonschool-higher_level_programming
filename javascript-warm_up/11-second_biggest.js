#!/usr/bin/node
const a = process.argv;
let p = 0;
for (let i = 2; i < a.length; i++) {
  if (p < parseInt(a[i])) {
    p = a[i];
  }
}
console.log(p -1);
