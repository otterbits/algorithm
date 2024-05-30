const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n").map(Number);

const n = input[0];
const dp = new Array({length: n + 1}, () => 0);

dp[1] = input[1];
dp[2] = input[1] + input[2];
dp[3] = Math.max(input[1] + input[3], input[2] + input[3]);

for (let i = 4; i <= n; i++) {
    dp[i] = Math.max(input[i] + input[i - 1] + dp[i - 3], input[i] + dp[i - 2]);
}

console.log(dp[n]);