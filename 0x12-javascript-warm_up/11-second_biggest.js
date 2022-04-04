#!/usr/bin/node
const process = require('process');
if (process.argv.length <= 3) {
  console.log('0');
} else {
  let s = 0;
  let x = parseInt(process.argv[1]);
  let y = parseInt(process.argv[2]);
  if (x < y) {
    s = x;
    x = y;
    y = s;
  }
  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] < x && process.argv[i] > y) {
      y = process.argv[i];
    }
  }
  console.log(y);
}
