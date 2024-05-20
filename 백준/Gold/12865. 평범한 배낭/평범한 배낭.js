const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [n, k] = input[0].split(" ").map(Number);
const stuffs = input.slice(1).map(stuff => stuff.split(" ").map(Number));
const dp = Array.from({length : n + 1}, () => Array(k + 1).fill(0));

for (let i = 1; i <= n; i ++){
    const [weight, value] = stuffs[i - 1];
    for (let capacity = 0; capacity <= k; capacity ++) {
        if (capacity - weight >= 0) {
            dp[i][capacity] = Math.max(dp[i - 1][capacity - weight] + value, dp[i - 1][capacity]);
        } else {
            dp[i][capacity] = dp[i - 1][capacity];
        }
    }
}
console.log(dp[n][k])