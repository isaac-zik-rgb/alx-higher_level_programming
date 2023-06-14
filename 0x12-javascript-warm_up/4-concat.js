#!/usr/bin/node
const str = 'is ';
const str1 = 'undefined';
if (process.argv) {
  if (process.argv.length === 2) {
    console.log('undefined ' + str + str1);
  } else if (process.argv.length === 3) {
    console.log(process.argv[2] + ' is ' + str1);
  } else console.log(process.argv[2] + ' is ' + process.argv[3]);
}
