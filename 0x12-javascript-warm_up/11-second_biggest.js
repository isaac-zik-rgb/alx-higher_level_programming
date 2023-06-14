#!/usr/bin/node
let firstLargest = process.argv[2];
if (process.argv.length <= 3){
    console.log(0);
    return;
}
for (let check = 2; check <= process.argv.length; check++){
    if (process.argv[check] > firstLargest){
	firstLargest = process.argv[check];
    }
}
let secondLargest =  process.argv[2];
for (let n = 2; n < process.argv.length; n++){
    if (process.argv[n] > secondLargest && process.argv[n] < firstLargest){
	secondLargest = process.argv[n];
    }
}
console.log(secondLargest);
