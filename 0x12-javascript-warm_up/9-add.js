#!/usr/bin/node
const process = require('process');
const arg = process.argv;

function add (a, b) {
  console.log(`${a + b}`);
}
add(Number(arg[2]), Number(arg[3]));
