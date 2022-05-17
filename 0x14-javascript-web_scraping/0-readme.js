#!/usr/bin/node
const fs = require('fs');
const myArgs = process.argv.slice(2);
fs.readFile(myArgs[0], (err, buff) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(buff.toString());
});
