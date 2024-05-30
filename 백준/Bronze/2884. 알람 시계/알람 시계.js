const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim();

let [h, m] = input.split(" ").map(Number);

const cyMinute = m - 45;

if (cyMinute < 0) {
    if (h === 0) {
        h = 23;
    } else {
    h --;
    }
    m = cyMinute + 60;
} else {
    m = cyMinute;
}

console.log(h, m);