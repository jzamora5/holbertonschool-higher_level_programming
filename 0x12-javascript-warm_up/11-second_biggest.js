#!/usr/bin/node
const nums = process.argv;

function secondMax (array) {
  if (array.length <= 3) {
    return (0);
  }

  array = array.slice(2).map(n => parseInt(n));

  const max = Math.max(...array);

  const arr = array.filter(arr => arr < max);

  return (Math.max(...arr));
}

console.log(secondMax(nums));
