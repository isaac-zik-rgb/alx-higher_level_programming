#!/usr/bin/node
const args = process.argv.slice(2); // Get the list of arguments excluding the script name

if (args.length === 0) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  const numbers = args.map(Number); // Convert arguments to an array of numbers
  const sortedNumbers = numbers.sort((a, b) => b - a); // Sort the numbers in descending order
  console.log(sortedNumbers[1]); // Print the second largest number
}
