const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt"
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = Number(input[0]);
const nums = input.slice(1).map((v) => v.split("").map(Number));

const quadTree = [];

const getQuadTree = (n, x, y) => {
    // 전체 합
    let total = 0;
    
    // 합 구하기
    for (let row = 0; row < n; row++) {
        for (let col = 0; col < n; col++) {
            total += nums[y + col][x + row];
        }
    }

    // 전체 합이 0이면 0
    if (total === 0) quadTree.push(0);
    // 전체 합이 n * n과 같으면(다 1일 때) 1
    else if (total === n * n) quadTree.push(1);
    else {
        // n을 1/2로 쪼개서 보기
        const next = n / 2;
        // 나누어진다면 괄호 열기
        quadTree.push("(");
        // 4면 하나하나씩 보기
        getQuadTree(next, x, y);
        getQuadTree(next, x + next, y);
        getQuadTree(next, x, y + next);
        getQuadTree(next, x + next, y + next);
        // 해당 4면의 결과값을 다 봤으면 괄호 닫기
        quadTree.push(")");
    }
}

getQuadTree(n, 0, 0);
console.log(quadTree.join(""));