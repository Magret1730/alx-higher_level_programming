#!/usr/bin/node

const fs = require('fs');

// Check if the correct number of command-line arguments is provided
if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

// Extract file paths from command-line arguments
const [, , fileA, fileB, fileC] = process.argv;

// Read the contents of fileA and fileB
const contentA = fs.readFileSync(fileA, 'utf-8');
const contentB = fs.readFileSync(fileB, 'utf-8');

// Concatenate the contents
const concatenatedContent = contentA + contentB;

// Write the concatenated content to fileC
fs.writeFileSync(fileC, concatenatedContent);

// console.log(`Contents of ${fileA} and ${fileB} are concatenated and written to ${fileC}`);
