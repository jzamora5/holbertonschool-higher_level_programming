#!/usr/bin/node
const argv = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2] + '/';
const request = require('request');

request(url, function (error, response, body) {
  if (error == null) {
    const rbody = JSON.parse(body);
    console.log(rbody.title);
  }
});
