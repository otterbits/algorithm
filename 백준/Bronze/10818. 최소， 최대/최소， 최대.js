const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = input.shift();
const form = input[0].split(" ").map(Number);

console.log(Math.min(...form), Math.max(...form));