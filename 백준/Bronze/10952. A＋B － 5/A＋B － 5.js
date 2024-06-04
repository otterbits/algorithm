const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

while (input.length) {
    let [a, b] = input.shift().split(" ").map(Number);
    a + b !== 0 ? console.log(a + b) : null;
}