#!/usr/bin/node
const fs = require('fs');
const txt1 = fs.readFileSync(process.argv[2]);
const txt2 = fs.readFileSync(process.argv[3]);
fs.writeFile(process.argv[4], txt1 + '\n' + txt2 + '\n', function (err) {
  if (err) throw err;
});
