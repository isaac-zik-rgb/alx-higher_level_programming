#!/usr/bin/node
const { writeFile } = require('fs');
const request = require('request');
const apiUrl = process.argv[2];
const filePath = process.argv[3];
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`${error}`);
    return;
  }
  if (response.statusCode !== 200) {
    console.log('Error:', `Recieved respons status code ${response.statusCode}`);
    return;
  }

  const fileContent = body;
  writeFile(filePath, fileContent, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
