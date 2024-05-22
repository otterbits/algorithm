const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const num = fs.readFileSync(filePath).toString().trim().split(" ").map(Number);

const [A, B] = num

console.log(A * B)