#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let str = '';
    for (let i = 0; i < this.width; i++) {
      str += 'X';
    }
    for (let j = 0; j < this.width; j++) {
      console.log(str);
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
