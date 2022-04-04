#!/usr/bin/node
const process = require('process');
if (process.argv.length <= 3) {
  console.log('0');
} else {
  let s = 0;
  let x = parseInt(process.argv[2]);
  let y = parseInt(process.argv[3]);
  if (x < y) {
    s = x;
    x = y;
    y = s;
  }
  for (let i = 2; i < process.argv.length; i++) {
    if ((parseInt(process.argv[i]) < x) && (parseInt(process.argv[i]) > y)) {
      y = parseInt(process.argv[i]);
    }
  }
  console.log(y);
}
