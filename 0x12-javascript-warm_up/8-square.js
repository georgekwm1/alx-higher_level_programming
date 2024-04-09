#!/usr/bin/node
const process = require('process');
const arg = process.argv;

if (arg[2] < 0) {

} else if (arg[2] > 0) {
  for (let count = 0; count < Number(arg[2]); count++) {
    console.log('x'.repeat(`${Number(arg[2])}`));
  }
} else {
  console.log('Missing size');
}
