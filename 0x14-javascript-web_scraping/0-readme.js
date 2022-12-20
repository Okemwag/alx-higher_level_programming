#!/usr/bin/node
const fs = require('fs');

// Get the file path from the command line argument
const filePath = process.argv[2];

// Read the file in utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // Print the error object if there was an error while reading the file
    console.error(err);
  } else {
    // Print the file content if the reading was successful
    console.log(data);
  }
});
