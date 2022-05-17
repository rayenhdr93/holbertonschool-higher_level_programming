#!/usr/bin/node
const fs = require('fs');
const myArgs = process.argv.slice(2);
fs.writeFile(myArgs[2], myArgs[3], (err) => {
  if (err) throw err;
});
