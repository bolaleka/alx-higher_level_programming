#!/usr/bin/node

const fs = require('fs');

// Get the file path from the command line arguments
const filePath = process.argv[2];

// Read the file in utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // If an error occurred during the reading, print the error object
    console.error(err);
  } else {
    // Print the content of the file
    console.log(data);
  }
});
