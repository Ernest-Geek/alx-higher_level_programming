#!/usr/bin/node
const args = process.argv.slice(2);
const count = args.length;
if (count === 0) {
  console.log('No argument');
} else if (count === 1) {
  console.log(args[0], args[1]);
} else if (count === 2) {
  console.log(`${args[0]} is ${args[1]}`);
} else {
  console.log('Argument found');
}
