#!/usr/bin/node

const num = parseInt(process.argv[2]);
let arr = '';

iif (/\d/.test(num) && process.argv[2] !== undefined && num > 0) {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      arr += 'X';
    }
    if (i !== num - 1) {
      arr += '\n';
    }
  }
  console.log(arr);
} else if (process.argv.length === 2 || !(/\d/.test(num))) {
  console.log('Missing size');
}
