#!/usr/bin/node
const { argv } = require('node:process');
if (isNaN(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let x = parseInt(argv[2]);
  while (x > 0) {
    console.log('C is fun');
    x--;
  }
}
