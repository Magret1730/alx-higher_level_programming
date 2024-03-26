#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.error('Status Code:', response.statusCode);
  } else {
    fs.writeFile(filePath, body, { encoding: 'utf-8' }, function (err) {
      if (err) {
        console.error('Error writing to file:', err);
      }
    });
  }
});
