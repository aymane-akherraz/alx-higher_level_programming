#!/usr/bin/node
function factoriel (nb) {
  if (nb === 0 || nb === 1) {
    return 1;
  }
  return nb * (factoriel(nb - 1));
}
const { argv } = require('node:process');
if (isNaN(argv[2])) {
  console.log(1);
} else {
  console.log(factoriel(parseInt(argv[2])));
}
