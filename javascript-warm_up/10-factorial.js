#!/usr/bin/node
function factorial (x) {

  if (isNaN(x)|| x === 0) {
    return 1;
  }
  return x * factorial(x - 1);
}
const arg1 = process.argv[2];

console.log(factorial(arg1));
