#!/usr/bin/node
/** script that prints the number of movies where the
 * character “Wedge Antilles” is present.
 */

const request = require('request');
const characterId = 18;
const apiURL = process.argv[2];

request(apiURL, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie data: ${response.statusCode}`);
  }

  const movies = JSON.parse(body).results; // converting to more readable format
  let numMovies = 0;

  // Loop through each movie
  movies.forEach(movie => {
    // Check if Wedge Antilles is present in the characters list
    const characters = movie.characters.map(character => parseInt(character.split('/').slice(-2)[0]));
    if (characters.includes(characterId)) {
      numMovies++;
    }
  });

  console.log(numMovies);
});
