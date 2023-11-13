#!/usr/bin/node
const args = process.argv.slice(2);
let count = 0;
for (; count < args.length; count++) {
// Looping without declaring any variable
}
if (count === 0) {
  console.log('No argument');
} else if (count === 1) {
  console.log(args[0]);
} else {
  console.log('Argument found');
}
