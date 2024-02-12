#!/usr/bin/node
const args = process.argv.slice(2);
const firstArg = parseInt(args[0]);

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n < 0) {
    return 0;
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const answer = factorial(firstArg);
console.log(answer);
