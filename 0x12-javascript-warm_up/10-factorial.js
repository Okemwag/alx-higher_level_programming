#!/usr/bin/node

function factorial (n) {
  const number = Number(n);
  if (isNaN(number)) {
    return 1;
  }
  if (n === 0) {
    return 1;
  }
  return n * factorial(number - 1);
}
console.log(factorial(process.argv[2]));
