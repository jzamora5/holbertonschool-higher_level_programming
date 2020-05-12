#!/usr/bin/node
const request = require('request');
const base64 = require('base-64');
const utf8 = require('utf8');

const consKey = process.argv[2];
const consSecret = process.argv[3];
const stSearch = process.argv[4];

const urlOauth2 = 'https://api.twitter.com/oauth2/token';
const urlSearch = 'https://api.twitter.com/1.1/search/tweets.json';

const brToken = `${consKey}:${consSecret}`;

const brToken64 = base64.encode(utf8.encode(brToken));

let options = {
  url: urlOauth2,
  headers: {
    Authorization: 'Basic ' + utf8.decode(brToken64), 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
  },
  form: { grant_type: 'client_credentials' }
};

request.post(options, function (error, response, body) {
  if (error == null) {
    const payload = JSON.parse(body);

    const acsToken = payload.access_token;

    const params = {
      q: stSearch,
      result_type: 'recent',
      count: 5
    };

    options = {
      url: urlSearch,
      headers: { Authorization: 'Bearer ' + acsToken },
      qs: params
    };

    request.get(options, function (error, response, body) {
      if (error == null) {
        const sbody = JSON.parse(body);
        for (const s of sbody.statuses) {
          const st = `[${s.id}] ${s.text} by ${s.user.name}`;
          console.log(st);
        }
      } else {
        console.log(error);
      }
    });
  } else {
    console.log(error);
  }
});
