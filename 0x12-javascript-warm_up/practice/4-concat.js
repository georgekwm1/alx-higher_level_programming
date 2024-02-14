#!/usr/bin/node
const { argv } = require('process');

if (argv[argv.length - 1] !== undefined) {
  console.log(`${argv[2]} is ${argv[3]}`);
}
