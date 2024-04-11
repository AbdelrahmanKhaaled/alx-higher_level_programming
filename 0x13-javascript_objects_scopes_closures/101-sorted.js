#!/usr/bin/node

exports.dict = require('./100-data').dict;

let newdic = {};
for (let [key, value] of Object.entries(dict)) {
	list = []
	for (let [key2, value2] of Object.entries(dict)) {
		if (value === value2)
			list.push(key2);
	}
	newdic[value] = list;
}

console.log(newdic);
