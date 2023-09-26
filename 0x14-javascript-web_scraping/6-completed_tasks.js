#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

// Initialize an empty object to store the count of completed tasks by user ID
const completedTasksByUser = {};

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Received response status code ${response.statusCode}`);
    return;
  }

  // Parse the JSON response
  const todos = JSON.parse(body);

  // Iterate through the todos and count completed tasks by user ID
  todos.forEach((todo) => {
    if (todo.completed) {
      if (completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId]++;
      } else {
        completedTasksByUser[todo.userId] = 1;
      }
    }
  });

  // Print the result as an object
  console.log(completedTasksByUser);
});
