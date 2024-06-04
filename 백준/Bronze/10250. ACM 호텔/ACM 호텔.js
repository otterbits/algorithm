const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = input.shift();

for (let i = 0; i < n; i++) {
    const data = input[i].split(" ").map(Number);
    const height = data[0];
    const cnt = data[2];
    let build = cnt % height === 0 ? height : cnt % height;
    let number = cnt % height === 0 ? cnt / height : Math.floor(cnt / height) + 1;
    number < 10 ? console.log(`${build}0${number}`) : console.log(`${build}${number}`);
}