#!/usr/bin/node

const oldDict = require('./101-data').dict;
// console.log(oldDict);

// Create a new dictionary to store user ids by occurrence
const occurrencesDict = {};

// Iterate over the original dictionary
for (const userId in oldDict) {
  const occurrences = oldDict[userId];
  // console.log(occurrences);

  // If the occurrences value is not already a key in the new
  // dictionary, create it
  if (!occurrencesDict[occurrences]) {
    occurrencesDict[occurrences] = [];
  }

  // Add the user id to the array corresponding to the occurrences value
  occurrencesDict[occurrences].push(userId);
}

// // Print the new dictionary
console.log(occurrencesDict);
