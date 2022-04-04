#!/usr/bin/node
function fact (n) {
  let x = n;
  for (let i = n - 1; i > 0; i--) {
    x = x * i;
  }
  console.log(x);
}
const process = require('process');
if (isNaN(process.argv[2])) {
  console.log('1');
} else {
  fact(process.argv[2]);
}
