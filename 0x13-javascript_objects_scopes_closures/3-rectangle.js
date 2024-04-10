#!/usr/bin/node

module.exports = class Rectangle {

	constructor(w,h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
	}

	print() {
		for (i = 0; i < this.width; i++) {
			if (i != this.width - 1) {
				process.stdout.write("X");
			else
				console.log("X");
			}
		}
	}
};
