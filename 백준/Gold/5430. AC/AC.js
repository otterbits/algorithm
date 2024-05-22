const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt"
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const num = input.shift();
for (let i = 0; i < input.length; i += 3) {
    let cmd = input[i]
    let arr = JSON.parse(input[i + 2])
    let isReverse = false;
    let isError = false;

    for (let nowCmd of cmd) {
        if (nowCmd === "R") {
            isReverse = !isReverse;
        } else if (nowCmd === "D") {
            if (arr.length === 0) {
                isError = true;
            }
            isReverse ? arr.pop() : arr.shift()
        }
    }
    console.log(isError ? "error" : JSON.stringify(isReverse ? arr.reverse() : arr))
}