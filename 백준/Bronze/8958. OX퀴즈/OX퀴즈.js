const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = input.shift();

for (let i = 0; i < n; i++) {
    let form = input.shift();
    let result = 0;
    let con = 0;
    for (let j = 0; j < form.length; j++) {
        
        if (form[j] === "O") {
            con ++;
            result += con;
        } else if (form[j] === "X") {
            con = 0;
        }
    }
    console.log(result);
}