#!/usr/bin/node

const callMeMoby = (x, p) => {
  for (let i = 0; i < x; i++) {
    p('C is fun');
  }
};

module.exports.callMeMoby = callMeMoby;
