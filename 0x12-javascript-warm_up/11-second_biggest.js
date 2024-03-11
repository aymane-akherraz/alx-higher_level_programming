#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length <= 3) {
  console.log(0);
} else {
  const list = [];
  argv.forEach((e, i) => {
    if (i > 1) {
      list.push(parseInt(e));
    }
  });
  console.log(list.sort(function (a, b) { return b - a; })[1]);
}
