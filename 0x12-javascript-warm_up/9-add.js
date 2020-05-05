#!/usr/bin/node
const argv = process.argv;
const x = parseInt(argv[2]);
const y = parseInt(argv[3]);

function add (a, b) {
  return (a + b);
}

console.log(add(x, y));
