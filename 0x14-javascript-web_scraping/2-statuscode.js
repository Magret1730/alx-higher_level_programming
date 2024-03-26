#!/usr/bin/node
// script that writes a string to a file.

const request = require('request');
const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.log(error);
  }
  console.log(`code: ${response.statusCode}`);
});
