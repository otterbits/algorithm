const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split(" ").map(Number);

let sum = 0;

for (num of input) {
    sum += num * num;
}

console.log(sum % 10)