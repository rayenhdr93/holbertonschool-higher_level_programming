#!/usr/bin/node
const process = require('process');
if (process.argv[2] && process.argv[3]) {
  console.log(process.argv[2], 'is', process.argv[3]);
} else {
  console.log('No argument');
}