#!/usr/bin/node

const process = require('process');
const arg = process.argv;

if (arg.length <= 2) {
  console.log('No argument');
} else {
  console.log(arg[2]);
}
