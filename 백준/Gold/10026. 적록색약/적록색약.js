const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const num = Number(input[0])
const grid = input.slice(1).map(v => v.split(""));

const dx = [1, 0, -1, 0];
const dy = [0, 1, 0, -1];

function getVisited () {
    return Array.from({length : num}, () => Array.from({length : num}, () => false));
}
let visited = getVisited();
let cntVisible = 0;
let cntInvisible = 0;

function dfs (x, y, visible) {
    let stack = [[x, y]]
    visited[x][y] = true;
    while (stack.length) {
        let [nowX, nowY] = stack.pop()
        for (let i = 0; i < 4; i++) {
            let nx = nowX + dx[i]
            let ny = nowY + dy[i]
            if (nx >= 0 && nx < num && ny >= 0 && ny < num && !visited[nx][ny]) {
                if (visible) {
                    if (grid[nowX][nowY] === grid[nx][ny]) {
                        visited[nx][ny] = true;
                        stack.push([nx, ny]);
                    }
                } else {
                    if ((grid[nowX][nowY] === 'R' && grid[nx][ny] === 'G') || (grid[nowX][nowY] === 'G' && grid[nx][ny] === 'R')) {
                        visited[nx][ny] = true;
                        stack.push([nx, ny]);
                    } else if (grid[nowX][nowY] === grid[nx][ny]) {
                        visited[nx][ny] = true;
                        stack.push([nx, ny]);
                    }
                }
            }
        }
    }
}

for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
        if (!visited[i][j]) {
            dfs(i, j, true);
            cntVisible ++;
        }
    }
}

visited = getVisited();

for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
        if (!visited[i][j]) {
            dfs(i, j, false);
            cntInvisible ++;
        }
    }
}

console.log(cntVisible, cntInvisible);