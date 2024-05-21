const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const num = fs.readFileSync(filePath).toString().trim().split(" ").map(Number);

const [a, b] = num

if (a > b) {
    console.log(">");
} else if (a == b) {
    console.log("==");
} else if (a < b) {
    console.log("<");
}