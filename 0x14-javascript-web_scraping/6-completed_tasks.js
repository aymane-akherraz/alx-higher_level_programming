#!/usr/bin/node
const request = require('request');

request(`${process.argv[2]}`, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const todos = JSON.parse(body);
  const myDict = {};
  todos.forEach(obj => {
    if (obj.completed === true) {
      myDict[`${obj.userId}`] = (myDict[`${obj.userId}`] || 0) + 1;
    }
  });
  console.log(myDict);
});
