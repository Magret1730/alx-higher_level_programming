#!/usr/bin/node
// script that writes a string to a file.

const request = require('request');
const movieId = process.argv[2];
const StarWarAPIEndpoint = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(StarWarAPIEndpoint, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie data: ${response.statusCode}`);
  }

  const movie = JSON.parse(body); // converting to more readable format
  console.log(movie.title);
});
