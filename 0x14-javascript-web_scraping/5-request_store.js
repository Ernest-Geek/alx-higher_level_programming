#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// Get the url and file path from the command line
const url = process.argv[2];
const filePath = process.argv[3];

// Make GET request to the url
request(url).pipe(fs.createWriteStream(filePath));
