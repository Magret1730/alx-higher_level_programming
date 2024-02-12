#!/usr/bin/node
const args = process.argv.slice(2);
const argsNumber = parseInt(args[0]);
// const argsNumber = Number(args[0]);
if (isNaN(argsNumber)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${argsNumber}`);
}
