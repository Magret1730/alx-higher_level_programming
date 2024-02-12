#!/usr/bin/node
const args = process.argv.slice(2);
const argsNumber = parseInt(args[0]);
if (isNaN(argsNumber)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < argsNumber; i++) console.log('C is fun');
}
