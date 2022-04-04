#!/usr/bin/node
const process = require('process');
let x = 0;
if (isNaN(process.argv[2]) || isNaN(process.argv[3])) {
  console.log('NaN');
} else {
  x = parseInt(process.argv[2]) + parseInt(process.argv[3]);
  console.log(x);
}
