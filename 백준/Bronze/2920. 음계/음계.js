const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split(" ").map(Number);

let cnt = 0;

for (let i = 0; i < 7; i ++) {
    if (input[i] < input[i+1]) {
        cnt++;
    }
}

const result = {
    0: 'descending',
    7: 'ascending',
}[cnt];

console.log(result || 'mixed');