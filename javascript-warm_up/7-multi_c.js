#!/usr/bin/node
const process = require('process');
const argument = +process.argv[2];
if (!argument) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < parseInt(argument); i++) {
  console.log('C is fun');
}
