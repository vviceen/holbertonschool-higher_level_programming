#!/usr/bin/node
let count = 0;
for (; process.argv[count] !== undefined; count++) {
  if (count === 2) {
    console.log(process.argv[2]);
  }
}
if (count < 3) {
  console.log('No argument');
}
