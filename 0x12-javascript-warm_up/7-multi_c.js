#!/usr/bin/node
let count = 0;
if (Number(process.argv[2])) {
  while (count < Number(process.argv[2])) {
    console.log('C is fun');
    count++;
  }
} else console.log('Missing number of occurrences');
