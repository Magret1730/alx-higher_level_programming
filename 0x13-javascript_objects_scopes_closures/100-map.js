#!/usr/bin/node

const myList = require('./100-data').list;
// console.log(myList);
const newList = myList.map((key, value) => value * key);
console.log(newList);
