#!/usr/bin/node
const request = require('request');

request(`${process.argv[2]}`, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const films = JSON.parse(body);
  let nbMovies = 0;
  films.results.forEach(obj => {
    if (obj.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      nbMovies++;
    }
  });
  console.log(nbMovies);
});
