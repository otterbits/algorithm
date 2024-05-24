const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const cnt = input.shift();
for (let i = 0; i < cnt; i++) {
    
    let [a, b] = input.shift().split(" ").map(Number);
    console.log(a + b);
}