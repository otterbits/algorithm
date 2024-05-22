const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const num = fs.readFileSync(filePath).toString().trim()

let lst = []

for (let i = 1; i <= num; i++) {
    lst.push("*".repeat(i));
}

lst.forEach(value => console.log(value.padStart(lst.length)))