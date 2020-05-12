#!/usr/bin/node
const argv = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/';
const id = argv[2];
const request = require('request');
request(`${url}${id}/`, function (error, response, body) {
  if (!error) {
    console.log(JSON.parse(body).title);
  }
});
