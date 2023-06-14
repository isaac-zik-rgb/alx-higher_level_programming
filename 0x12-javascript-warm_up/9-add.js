#!/usr/bin/node
function add(a, b){
    return Number(process.argv[2]) + Number(process.argv[3]);
}


console.log(add(Number(process.argv[2]), Number(process.argv[2])));
