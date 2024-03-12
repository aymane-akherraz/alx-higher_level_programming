#!/usr/bin/node

const dict = require('./101-data').dict;
const Keys = [...new Set(Object.values(dict))];
const newDict = {};
Keys.forEach(e => {
  newDict[e] = Object.entries(dict).filter(([key, value]) => e === value)
    .map(([key, value]) => key);
});
console.log(newDict);
