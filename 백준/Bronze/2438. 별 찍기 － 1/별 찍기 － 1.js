const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const num = fs.readFileSync(filePath).toString().trim()

for (let i = 1; i <= num; i++) {
    console.log("*".repeat(i));
}