const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

// 테스트 케이스 개수
const tc = input.shift();

const directions = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1]
]

function dfs (x, y, row, col, field, visited) {
    let stack = [[x, y]]
    visited[x][y] = true;
    while (stack.length) {
        let [nowX, nowY] = stack.pop();
        visited[nowX][nowY] = true;

        // 상하좌우 탐색
        for (let [dx, dy] of directions) {
            let nx = nowX + dx;
            let ny = nowY + dy;
            // 해당 위치가 밭 안이고, 방문하지 않았고, 배추가 있다면
            if ((nx >= 0 && nx < col && ny >= 0 && ny < row) && !visited[nx][ny] && field[nx][ny] === 1) {
                stack.push([nx, ny]);
                visited[nx][ny] = true;
            }
        }
    }
}

for (let i = 0; i < tc; i++) {

    let [row, col, locCnt] = input.shift().split(" ");
    let location = input.splice(0, locCnt);
    let field = Array.from({length: col}, () => Array.from({length: row}, () => 0));

    for (loc of location) {
        let [locY, locX] = loc.split(" ").map(Number);
        field[locX][locY] = 1;
    }
    let visited = Array.from({length: col}, () => Array.from({length: row}, () => false));

    let cnt = 0;

    for (loc of location) {
        let [locY, locX] = loc.split(" ").map(Number);
        if (!visited[locX][locY]) {
            dfs(locX, locY, row, col, field, visited);
            cnt ++;
        }
    }

    console.log(cnt);
}
