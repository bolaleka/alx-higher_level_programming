#!/usr/bin/node

function add (a, b) {
  let res = 0;
  if (process.argv.length !== 4) {
    console.log('NaN');
  } else {
    res = a + b;
    console.log(res);
  }
}
add(parseInt(process.argv[2]), parseInt(process.argv[3]));
