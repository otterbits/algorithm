const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt"
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = input.shift();

const score = input.shift().split(" ");
const maxScore = Math.max(...score);

for (let i = 0; i < n; i++) {
    score[i] = score[i] / maxScore * 100
}

let scoreAverage = score.reduce((a, b) => a + b, 0) / n;
console.log(scoreAverage);