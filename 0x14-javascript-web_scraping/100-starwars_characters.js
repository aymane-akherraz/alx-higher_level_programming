#!/usr/bin/node
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const chars = JSON.parse(body);
  chars.characters.forEach(url => {
    request(`${url}`, (err, res, data) => {
      if (err) {
        console.error(err);
        return;
      }
      const character = JSON.parse(data);
      console.log(character.name);
    });
  });
});
