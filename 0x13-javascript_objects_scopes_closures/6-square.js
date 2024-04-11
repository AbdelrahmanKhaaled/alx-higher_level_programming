#!/usr/bin/node

const SquareOld = require('./5-square');

class Square extends SquareOld {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      let str = '';
      for (let j = 0; j < this.size; j++) {
        if (c === undefined)
          c = "X";
	str += 'X';
      }
      console.log(str);
    }
  }
}

module.exports = Square;
