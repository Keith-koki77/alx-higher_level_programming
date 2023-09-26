#!/usr/bin/node
//Script that computes the number of tasks completed by user id.

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node 6-completed_tasks.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

const completedTasksByUser = {};

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Error:', `Status Code ${response.statusCode}`);
    process.exit(1);
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
