#!/usr/bin/node
console.log(factorial(process.argv[2]));
function factorial (num) {
  if (!num) {
    return 1;
  }
  if (num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
