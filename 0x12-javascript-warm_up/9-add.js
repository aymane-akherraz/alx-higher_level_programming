#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const { argv } = require('node:process');
if (isNaN(argv[2]) || isNaN(argv[3])) {
  console.log('NaN');
} else {
  console.log(add(parseInt(argv[2]), parseInt(argv[3])));
}
