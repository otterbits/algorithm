const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

let [num, amount] = input.shift().split(" ").map(Number);

const value = input.map(Number);
let cnt = 0;

for (let v = num - 1; v >= 0; v--) {
    cnt += Math.floor(amount / value[v]);
    amount %= value[v];
}

console.log(cnt);