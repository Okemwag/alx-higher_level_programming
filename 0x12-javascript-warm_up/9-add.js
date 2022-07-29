#!/usr/bin/node
const arg1 = Number(process.argv[2]);
const arg2 = Number(process.argv[3]);

function add (a, b) {
  if (a && b) {
    return (a + b);
  }
  return NaN;
}
console.log(add(arg1, arg2));
