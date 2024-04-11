#!/usr/bin/node

exports.list = require('./100-data');

let listMap = list.map(function (element, index) {return element * index});

console.log(list);
console.log(listMap);
