const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [n, x] = input.shift().split(" ").map(Number);

const nums = input.shift().split(" ").map(Number);

let answer = '';

for (num of nums) {
    if (num < x) {
        answer += num + ' ';
    }
}
console.log(answer);

