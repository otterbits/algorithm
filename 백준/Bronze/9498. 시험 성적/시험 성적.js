const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const num = fs.readFileSync(filePath).toString().trim()

if (num >= 90) {
    console.log("A");
} else if (num >= 80) {
    console.log("B");
} else if (num >= 70) {
    console.log("C");
} else if (num >= 60) {
    console.log("D");
} else {
    console.log("F");
}