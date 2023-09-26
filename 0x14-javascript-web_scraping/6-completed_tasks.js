#!/usr/bin/node
//Script that computes the number of tasks completed by user id.

const request = require('request');

// Check if the correct number of command-line arguments are provided
if (process.argv.length !== 3) {
  console.error('Usage: node 6-completed_tasks.js <API_URL>');
  process.exit(1);
}

// Get the API URL from the command-line argument
const apiUrl = process.argv[2];

// Initialize an object to store the count of completed tasks per user
const completedTasksByUser = {};

// Make an HTTP GET request to the specified API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Error:', `Status Code ${response.statusCode}`);
    process.exit(1);
  }

  // Parse the JSON response
  const todos = JSON.parse(body);

  // Iterate through the todos and count completed tasks per user
  todos.forEach((todo) => {
    if (todo.completed) {
      if (completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId]++;
      } else {
        completedTasksByUser[todo.userId] = 1;
      }
    }
  });

  // Print the completed tasks count per user
  console.log(completedTasksByUser);
});
