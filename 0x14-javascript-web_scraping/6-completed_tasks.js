#!/usr/bin/node
// script that computes the number of tasks completed by user id

const request = require('request');
const apiURL = process.argv[2];

request(apiURL, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie data: ${response.statusCode}`);
  }

  const todos = JSON.parse(body); // converting to more readable format
  const completedTask = {};

  todos.forEach((todo) => {
    if (todo.completed) {
      if (completedTask[todo.userId]) {
        completedTask[todo.userId]++;
      } else {
        completedTask[todo.userId] = 1;
      }
    }
  });
  console.log(completedTask);
});
