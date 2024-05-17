const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt"
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [row, col] = input[0].split(" ").map(Number);
const graph = input.slice(1).map((v) => v.split(" ").map(Number));
const dx = [1, 0, -1, 0]
const dy = [0, 1, 0, -1]

function getTomatoDay(row, col, graph) {
    const queue = [];
    const dist = [...Array(col)].map(() => Array(row).fill(0));

    for (let i = 0; i < col; i++) {
        for (let j = 0; j < row; j++) {
            if (graph[i][j] === 1) {
                queue.push([i, j]);
            } else if (graph[i][j] === 0) {
                dist[i][j] = -1;
            }
        }
    }

    let head = 0;
    while (queue.length > head) {
        const [x, y] = queue[head];
        head++;
        for (let k = 0; k < 4; k++) {
            const nx = x + dx[k];
            const ny = y + dy[k];
            if (nx < 0 || ny < 0 || nx >= col || ny >= row) continue;
            if (dist[nx][ny] >= 0) continue;

            dist[nx][ny] = dist[x][y] + 1;

            queue.push([nx, ny]);
        }
        
    }

    let day = 0;
    for (let i = 0; i < col; i++) {
        for (let j = 0; j < row; j++) {
            if (dist[i][j] === -1) return -1;
            day = Math.max(day, dist[i][j]);
        }
    }
    return day;
}


console.log(getTomatoDay(row, col, graph));