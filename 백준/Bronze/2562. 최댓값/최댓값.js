const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n").map(Number);

const maxNum = Math.max(...input);
const order = input.findIndex(num => num === maxNum) + 1;

console.log(maxNum);
console.log(order);