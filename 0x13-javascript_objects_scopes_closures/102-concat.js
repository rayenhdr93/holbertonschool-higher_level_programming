#!/usr/bin/node
const process = require('process');
const fs = require('fs');
let txt1 = '';
if (process.argv.length === 5) {
  fs.readFile(process.argv[2], (err, data) => {
    if (err) throw err;

    txt1 = data;
  });
  fs.readFile(process.argv[3], (err, data) => {
    if (err) throw err;
    txt1 = txt1 + '\n' + data + '\n';
    fs.writeFile(process.argv[4], txt1, (err) => {
      if (err) throw err;
    });
  });
}
