#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');
const fileA = argv[2];
const fileB = argv[3];
const fileC = argv[4];

const fileRead = (file) => {
  return new Promise((resolve, reject) => {
    fs.readFile(file, 'utf8', (err, data) => {
      if (err) {
        reject(err);
      } else {
        resolve(data);
      }
    });
  });
};

const promises = [fileA, fileB].map(fileRead);

Promise
  .all(promises)
  .then(resolve => {
    const Concat = resolve.join('');
    fs.writeFile(fileC, Concat, (err) => {
      if (err) throw err;
    });
  })
  .catch(err => console.log(err));
