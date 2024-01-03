#!/usr/bin/node
// fs: Provides method for working with file systems
const fs = require('fs');

// Read the file path argument
const filePath = process.argv[2];

// Read the path using utf8 encoding
fs.readFile(filePath, 'utf8', (error, data) => console.log(error || data));
