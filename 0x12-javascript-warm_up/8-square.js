#!/usr/bin/node

let square = '';
if (Number(process.argv[2])) {
  for (let count = 0; count < Number(process.argv[2]); count++) {
    square = ' ';
    for (let i = 0; i < Number(process.argv[2]); i++) {
      square += 'x';
    }
    console.log(square);
  }
} else console.log('Missing size');
