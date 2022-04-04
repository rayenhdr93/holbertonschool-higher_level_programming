#!/usr/bin/node
const process = require('process');
if (process.argv.length <= 3) {
  console.log('0');
} else {
  let s = 0;
  let x = (process.argv[2]);
  let y = (process.argv[3]);
  if (x < y) {
    s = x;
    x = y;
    y = s;
  }
  for (let i = 4; i < process.argv.length + 1; i++) {
    if ((process.argv[i] > x)) {
      y = x;
      x = process.argv[i];
    }
    if ((process.argv[i] < x) && (process.argv[i] > y)) {
      y = process.argv[i];
    }
  }
  console.log(y);
}
