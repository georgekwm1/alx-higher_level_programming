#!/usr/bin/node
const process = require('process');
const arg = process.argv;
if (!isNaN(arg[2])) {
  console.log(`My number: ${arg[2]}`);
} else { console.log('Not a number'); }
