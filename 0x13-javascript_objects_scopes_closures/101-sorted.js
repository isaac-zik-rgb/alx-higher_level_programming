#!/usr/bin/node
const { dict } = require('./101-data');

const newDict = {};

for (const keys in dict) {
  const value = dict[keys];

  if (!newDict[value]) {
    newDict[value] = [keys];
  } else {
    newDict[value].push(keys);
  }
}
console.log(newDict);
