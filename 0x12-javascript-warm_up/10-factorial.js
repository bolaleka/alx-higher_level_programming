#!/usr/bin/node

function fact (num) {
  if (num === 0 || process.argv.length === 2) {
    return (1);
  } else {
    return (num * fact(num - 1));
  }
}
console.log(fact(process.argv[2]));
