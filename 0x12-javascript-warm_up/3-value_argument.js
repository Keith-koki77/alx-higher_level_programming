#!/usr/bin/node
const firstArgs = process.argv.slice(2);

if (firstArgs[0]) {
  console.log(firstArgs[0]);
} else {
  console.log("No argument");
}
