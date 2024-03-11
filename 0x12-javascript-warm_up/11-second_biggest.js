#!/usr/bin/node
const { argv } = require('node:process');
const list = [];
if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  argv.forEach((e, i) => {
    if (i > 1) {
      list.push(parseInt(e));
    }
  });
  let m = list[0];
  const len = list.length;
  let i = 1;
  while (i < len) {
    if (list[i] > m) {
      m = list[i];
    }
    i++;
  }
  let sm = list[0];
  i = 1;
  while (i < len) {
    if (list[i] > sm && list[i] !== m) {
      sm = list[i];
    }
    i++;
  }
  console.log(sm);
}
