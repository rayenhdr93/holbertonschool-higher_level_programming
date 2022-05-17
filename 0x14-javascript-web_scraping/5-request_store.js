#!/usr/bin/node
const fs = require('fs');
const axios = require('axios').default;
const process = require('process');
axios.get(process.argv[2])
  .then(function (response) {
    fs.writeFile(process.argv[3], response.data, (err) => {
      if (err) throw err;
    });
  });
