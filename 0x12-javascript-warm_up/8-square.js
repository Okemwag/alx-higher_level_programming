#!/usr/bin/node
const square = Number(process.argv[2]);
if (square) {
  for (let i = 0; i < square; i++) {
    console.log('X'.repeat(square));
  }
} else {
  console.log('Missing size');
}
