#!/usr/bin/node
const args = process.argv;
let largest = 0;
let next = 0;
let num;
if (args.length < 4) {
  console.log('0');
} else {
  for (let i = 2; i < args.length; i++) {
    num = Number(args[i]);
    if (num > largest) {
      next = largest;
      largest = num;
    } else if (num > next) {
      next = num;
    }
  }
  console.log(next);
}
