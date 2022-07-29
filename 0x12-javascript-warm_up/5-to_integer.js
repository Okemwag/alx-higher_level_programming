#!/usr/bin/node

const converted = Number(process.argv[2]);
if (converted) {
  console.log('My number: ' + converted);
} else {
  console.log('Not a number');
}
