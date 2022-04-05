#!/usr/bin/node
const array1 = require('./100-data.js').list;
const map1 = [];
console.log(array1);
for (let i = 0; i < array1.length; i++) {
  if (i === 0) {
    map1[i] = 0;
  } else {
    map1[i] = array1[i] * array1[i - 1];
  }
}
console.log(map1);
