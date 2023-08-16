#!/usr/bin/node
const fs = require('fs');

const args = process.argv.slice(2);

const filePath1 = args[0];
const filePath2 = args[1];
const outputPath = args[2];

const contentFile1 = fs.readFileSync(filePath1, 'utf8');
const contentFile2 = fs.readFileSync(filePath2, 'utf8');

const concatFile = contentFile1 + contentFile2;

fs.writeFileSync(outputPath, concatFile);
