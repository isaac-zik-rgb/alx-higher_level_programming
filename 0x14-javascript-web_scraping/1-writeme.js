#!/usr/bin/node
const { writeFile } = require('fs')
const filePath = process.argv[2];
const fileContent = process.argv[3]
writeFile(filePath, fileContent, 'utf-8', (err) => {
    if (err){
        console.log(err);
        return;
    }
});
