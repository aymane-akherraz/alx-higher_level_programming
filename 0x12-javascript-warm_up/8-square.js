#!/usr/bin/node
const { argv } = require('node:process');
if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  const size = parseInt(argv[2]);
  let height = size;
  while (height > 0) {
    let square = '';
    let width = size;
    while (width > 0) {
      square += 'X';
      width--;
    }
    console.log(square);
    height--;
  }
}
