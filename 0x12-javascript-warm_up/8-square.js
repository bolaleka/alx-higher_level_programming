#!/usr/bin/node

const num = parseInt(process.argv[2]);
let arr = '';

if (num <= 0) {
  console.log();
}

if (/\d/.test(num) && process.argv[2] !== undefined) {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      arr += 'x';
    }
    if (i !== num - 1) {
      arr += '\n';
    }
  }
  console.log(arr);
} else {
  console.log('Missing size');
}
