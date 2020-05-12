#!/usr/bin/node
const argv = process.argv;
const url = argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const rbody = JSON.parse(body);
    const dict = {};
    for (const i of rbody) {
      if (!dict[i.userId]) {
        dict[i.userId] = 0;
      }
      if (i.completed) {
        dict[i.userId] += 1;
      }
    }
    console.log(dict);
  }
});
