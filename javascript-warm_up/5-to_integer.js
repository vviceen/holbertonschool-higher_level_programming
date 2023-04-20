#!/usr/bin/node
const num1 = parseInt(process.argv[2]);
if (!isNaN(num1) && typeof num1 === 'number') {
  console.log('My number:', num1);
} else {
  console.log('Not a number');
}
