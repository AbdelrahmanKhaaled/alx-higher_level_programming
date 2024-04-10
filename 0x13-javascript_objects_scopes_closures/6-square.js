#!/usr/bin/node

const SquareOld = require('./5-square');

module.exports = class Square extends SquareOld {

	constructor(size) {
		super(size);
		this.size = size;
	}

	charPrint(c) {
		for (let i = 0; i < this.size; i++) {
			for (let j = 0; j < this.size; j++) {
				if (c === undefined)
					c = "X";
				if (j != this.size - 1)
					process.stdout.write(c);
				else
					console.log(c);
			}
		}
	}
}
