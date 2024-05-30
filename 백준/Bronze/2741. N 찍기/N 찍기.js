const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim();

let answer = '';

for (let i = 1; i<=input; i++) {
    answer += i + '\n';
}

console.log(answer);
