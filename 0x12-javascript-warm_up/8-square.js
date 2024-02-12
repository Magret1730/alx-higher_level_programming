#!/usr/bin/node
const args = process.argv.slice(2);
const valSquare = parseInt(args[0]);
if (isNaN(valSquare)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < valSquare; i++) {
    let row = '';
    for (let j = 0; j < valSquare; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
