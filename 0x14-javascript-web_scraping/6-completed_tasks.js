#!/usr/bin/node
const request = require('request');

// Get API URL from the commalnd line argument
const apiUrl = process.argv[2];

// Make a GET request from the specified API endpoint
request.get(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const tasksData = JSON.parse(body);

    // filter tasks with completed status
    const completedTasks = tasksData.filter((task) => task.completed);

    // Count completed tasks for each user
    const completedTasksByUser = completedTasks.reduce((countByUser, task) => {
      countByUser[task.userId] = (countByUser[task.userId] || 0) + 1;
      return countByUser;
    }, {});

    // Print the result
    console.log(completedTasksByUser);
  } else {
    console.error(`Error: ${error}`);
  }
});
