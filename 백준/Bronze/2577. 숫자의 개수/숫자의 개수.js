    const fs = require("fs");
    const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
    const input = fs.readFileSync(filePath).toString().trim().split("\n").map(Number);

    let multiply = 1;

    for (num of input) {
        multiply *= num;
    }
    const cnt = Array.from({length: 10}, () => 0);

    let arr  = multiply.toString().split("").map(Number);

    for (n of arr) {
        cnt[n] ++;
    }

    for (c of cnt) {
        console.log(c);
    }
