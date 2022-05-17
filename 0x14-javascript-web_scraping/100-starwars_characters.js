#!/usr/bin/node
const axios = require('axios').default;
const process = require('process');
const x = process.argv[2];
axios.get('https://swapi-api.hbtn.io/api/films/')
  .then(function (response) {
    for (let y = 0; y < response.data.results[x - 1].characters.length; y++) {
      axios.get(response.data.results[x - 1].characters[y])
        .then(function (response2) {
          console.log(response2.data.name);
        });
    }
  }
  );
