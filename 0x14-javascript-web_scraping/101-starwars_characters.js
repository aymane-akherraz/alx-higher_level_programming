#!/usr/bin/node
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, async (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const chars = JSON.parse(body).characters;
  for (const url of chars) {
    try {
      const characterData = await requestData(url);
      console.log(characterData.name);
    } catch (err) {
      console.error(err);
    }
  }
});

function requestData (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res, data) => {
      if (err) {
        reject(err);
        return;
      }
      resolve(JSON.parse(data));
    });
  });
}
