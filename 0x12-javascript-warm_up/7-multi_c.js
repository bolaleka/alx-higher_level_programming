#!/usr/bin/node

let arg = parseInt(process.argv[2]);

if (process.argv.length === 2) {
  console.log('Missing number of occurrences');
} else if (process.argv.length === 3 && arg > 0) {
  while (arg > 0) {
    console.log('C is fun');
    arg--;
  }
}
