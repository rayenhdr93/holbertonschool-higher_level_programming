#!/usr/bin/node
const axios = require('axios').default;
const myArgs = process.argv.slice(2);
axios.get(myArgs[0])
  .catch(function (error) {
    console.log('code:', error.response.status);
  });
