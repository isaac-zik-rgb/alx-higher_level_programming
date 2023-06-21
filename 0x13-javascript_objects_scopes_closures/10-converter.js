#!/usr/bin/node
exports.converter = function (base){
    num => return num.toString(base);
};
