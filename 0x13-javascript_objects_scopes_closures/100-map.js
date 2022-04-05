#!/usr/bin/node
const array1 = require('./100-data.js').list;
let i = 0;
console.log(array1);
const map1 = array1.map(x => x * i++);
console.log(map1);
