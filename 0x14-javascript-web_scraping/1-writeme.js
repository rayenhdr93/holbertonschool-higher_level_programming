#!/usr/bin/node
const fs = require('fs');
const myArgs = process.argv.slice(2);
fs.writeFile(myArgs[0], '\ufeff' + myArgs[1], function (err) {
  if (err) return console.log(err);
});
