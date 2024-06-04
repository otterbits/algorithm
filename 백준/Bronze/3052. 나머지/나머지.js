const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const result = new Set([]);
for (n of input) {
    result.add(n % 42);
}

console.log(result.size);