#!/usr/bin/node
const argv = process.argv;
const url = argv[2];
const urlChar = 'https://swapi-api.hbtn.io/api/people/18/';
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    try {
      const rbody = JSON.parse(body);
      let count = 0;
      for (const i of rbody.results) {
        if (i.characters.includes(urlChar)) {
          count++;
        }
      }
      console.log(count);
    } catch (err) {
      console.error('error:', err);
    }
  }
});
