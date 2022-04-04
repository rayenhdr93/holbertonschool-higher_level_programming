#!/usr/bin/node
const process = require('process');
let txt = '';
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    txt += 'X';
  }
  for (let i = 0; i < process.argv[2]; i++) {
    console.log(txt);
  }
}
