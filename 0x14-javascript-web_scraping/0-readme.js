#!/usr/bin/node
const { readFile } = require('fs');
const filePath = process.argv[2];

readFile(filePath, 'utf-8', (err, result) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(result);
});
