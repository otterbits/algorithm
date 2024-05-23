const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n").map(Number);

const num = input.shift();

memoZero = [1, 0, 1];
memoOne = [0, 1, 1];

for (let i = 2; i <= Math.max(...input); i++) {
    memoZero[i] = memoZero[i - 1] + memoZero[i - 2];
    memoOne[i] = memoOne[i - 1] + memoOne[i - 2];
}

for (number of input) {
    console.log(memoZero[number] + " " + memoOne[number]);
}