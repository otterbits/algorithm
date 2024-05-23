const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n").map(Number);

num = input.shift()

const memo = [0];

memo[1] = 1;
memo[2] = 2;
memo[3] = 4;

for (let i = 4; i <= Math.max(...input); i++) {
    memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3];
}

for (num of input) {
    console.log(memo[num])
}