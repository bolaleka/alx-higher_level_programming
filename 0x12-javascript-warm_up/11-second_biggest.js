#!/usr/bin/node

const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  const arr = [];
  let j = 2;
  for (let i = 0; i < (args.length - 2); i++) {
    arr.push(args[j]);
    j++;
  }
  arr.sort();
  console.log(arr[arr.length - 2]);
}
