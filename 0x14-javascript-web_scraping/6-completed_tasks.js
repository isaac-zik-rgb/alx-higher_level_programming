#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';
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

  const todos = JSON.parse(body);

  todos.forEach((todo) => {
    if (todo.completed) {
      if (completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId]++;
      } else {
        completedTasksByUser[todo.userId] = 1;
      }
    }
  });

  console.log(completedTasksByUser);
});
