#!/usr/bin/node
const argv = process.argv;
const urlFilm = 'https://swapi-api.hbtn.io/api/films/';
const urlMovie = `${urlFilm}${argv[2]}/`;

const request = require('request');

request(urlMovie, function (error, response, body) {
  if (!error) {
    const fbody = JSON.parse(body);
    const characters = fbody.characters;
    const limit = characters.length;

    if (characters.length > 0) {
      CharRequest(0, characters[0], characters, limit);
    }
  } else {
    console.error('error:', error);
  }
});

function CharRequest (idx, url, characters, limit) {
  if (idx === limit) { return; }
  request(url, function (error, response, body) {
    if (!error) {
      const rbody = JSON.parse(body);
      console.log(rbody.name);
      idx++;
      CharRequest(idx, characters[idx], characters, limit);
    } else {
      console.error('error:', error);
    }
  });
}
