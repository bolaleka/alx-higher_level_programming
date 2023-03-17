#!/usr/bin/node

function print () {
  return ('C is fun');
}
const callMeMoby = (x, print) => {
  for (let i = 0; i < x; i++) {
    print();
  }
};

module.exports.callMeMoby = callMeMoby;
