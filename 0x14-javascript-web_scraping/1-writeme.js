#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');
const fileName = argv[2];
const string = argv[3];
fs.writeFile(fileName, string, function (err) {
  if (err) return console.log(err);
});
