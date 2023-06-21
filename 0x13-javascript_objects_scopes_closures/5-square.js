#!/usr/bin/node
const Square = require('./5-square');

class Square extends Rectangle{
    constructor(size){
	super(size, size);
    }
}
module.exports = Square;
