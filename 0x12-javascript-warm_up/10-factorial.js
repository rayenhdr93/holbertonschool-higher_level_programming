#!/usr/bin/node
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const process = require('process');
if (isNaN(process.argv[2])) {
  console.log('1');
} else { console.log(factorial(process.argv[2])); }
