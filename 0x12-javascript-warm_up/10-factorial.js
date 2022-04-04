#!/usr/bin/node
function factorial (n) {
  let answer = 1;
  if (n === 0 || n === 1) {
    return answer;
  } else {
    for (let i = n; i >= 1; i--) {
      answer = answer * i;
    }
    return answer;
  }
}
const process = require('process');
if (isNaN(process.argv[2])) {
  console.log('NaN');
} else { console.log(factorial(process.argv[2])); }
