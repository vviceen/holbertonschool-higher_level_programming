#!/usr/bin/node
const process = require('process');
const argument = +process.argv[2];
if (!argument) {
  console.log('Missing size');
}
for (let i = 0; i < argument; i++) {
  console.log('X'.repeat(argument));
}
