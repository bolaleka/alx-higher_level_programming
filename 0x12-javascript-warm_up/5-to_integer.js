#!/usr/bin/node

const parse = process.argv[2];

if (/\d/.test(parse) && process.argv[2] !== undefined) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
