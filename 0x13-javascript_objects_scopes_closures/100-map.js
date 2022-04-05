#!/usr/bin/node
const array1 = require('./100-data.js').list;
console.log(array1);
const map1 = array1.map(x => x * (x - 1));
console.log(map1);
