#!/usr/bin/node

// script that computes the number of tasks completed by user id
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const tasks = JSON.parse(body);

  const completedTasks = {};

  for (const task of tasks) {
    if (task.completed) {
      if (completedTasks[task.userId]) {
        completedTasks[task.userId]++;
      } else {
        completedTasks[task.userId] = 1;
      }
    }
  }

  console.log(completedTasks);
});
