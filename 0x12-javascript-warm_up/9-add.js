#!/usr/bin/node
const args = process.argv.slice(2);
const args0 = parseInt(args[0]);
const args1 = parseInt(args[1]);
function add (a, b) {
  return a + b;
}
console.log(add(args0, args1));
