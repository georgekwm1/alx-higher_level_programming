#!/usr/bin/node
const { argv } = require('process');

const str = argv[2];
const num = parseInt(str);
if (!isNaN(num)) {
  console.log(`My number: ${str}`);
} else {
  console.log('Not a number');
}
