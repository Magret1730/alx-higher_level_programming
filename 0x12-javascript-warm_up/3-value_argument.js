#!/usr/bin/node
const args = process.argv.slice(2);
if (args < 1) {
  console.log('No argument');
} else {
  console.log(`${args}`);
}
