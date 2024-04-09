#!/usr/bin/node
const process = require('process');
const array = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

for (let count = 0; count < array.length; count++) {
  const element = array[count];
  console.log(`${element}`);
}
