#!/usr/bin/node
const args = process.argv.slice(2);
const count = args.length;

if (count === 0) {
  console.log('Not a number');
} else if (count === 1) {
  // parseInt(Passes a string arg and returns an int)
  const intValue = parseInt(args[0], 10);
  if (!isNaN(intValue)) {
    console.log(`My number: ${intValue}`);
  } else {
    console.log('Not a number');
  }
} else {
  console.log(`${args[0]} is ${args[1]}`);
}
