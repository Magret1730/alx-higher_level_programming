#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status Code:', response.statusCode);
  } else {
    const movie = JSON.parse(body);
    const charactersUrls = movie.characters;

    // Function to fetch character data and print name
    const fetchAndPrintCharacter = (url) => {
      request(url, function (error, response, body) {
        if (error) {
          console.error('Error:', error);
        } else if (response.statusCode !== 200) {
          console.error('Status Code:', response.statusCode);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    };

    // Loop through character URLs and fetch/print them
    charactersUrls.forEach(characterUrl => {
      fetchAndPrintCharacter(characterUrl);
    });
  }
});
