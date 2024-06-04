const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const str = input[0];
const num = input[1] - 1;

console.log(str[num]);
