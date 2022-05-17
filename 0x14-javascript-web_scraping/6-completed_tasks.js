#!/usr/bin/node
const axios = require('axios').default;
axios.get('https://jsonplaceholder.typicode.com/todos')
  .then(function (response) {
    const dict = {};
    for (let x = 0; x < response.data.length; x++) {
      if (response.data[x].completed === true) {
        dict[response.data[x].userId] = 0;
      }
    }
    for (let x = 0; x < response.data.length; x++) {
      if (response.data[x].completed === true) {
        dict[response.data[x].userId] = dict[response.data[x].userId] + 1;
      }
    }
    console.log(dict);
  })
  .catch(function (error) {
    console.log(error);
  });
