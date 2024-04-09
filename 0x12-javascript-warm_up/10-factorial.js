#!/usr/bin/node
const process = require('process');
const arg = process.argv;
function factorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return (Number(n) * factorial(Number(n) - 1));
  }
}
console.log(factorial(Number(arg[2])));
