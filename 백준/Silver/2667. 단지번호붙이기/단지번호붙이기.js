const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const num = Number(input.shift());

const guidance = input.map(v => v.split(''));

let visited = Array.from({length: num}, () => Array.from({length: num}, () => false));

const dx = [1, 0, -1, 0];
const dy = [0, 1, 0, -1];

function dfs (x, y) {
    // 단지내 집 수 카운트 (default가 1인 이유는 이미 해당 지점 탐색을 시작할 때 그 지점의 집을 세아리기 때문)
    let cnt = 1;
    let stack = [[x, y]];
    visited[x][y] = true;

    while (stack.length) {
        let [nowX, nowY] = stack.pop();

        for (let i = 0; i < 4; i++) {
            let nx = nowX + dx[i];
            let ny = nowY + dy[i];
        
            // 지도 안에 있고, 아직 방문하지 않았고, 집이 있는 곳일 경우
            if (nx >= 0 && nx < num && ny >= 0 && ny < num && !visited[nx][ny] && guidance[nx][ny] === "1") {
                visited[nx][ny] = true;
                cnt ++;
                stack.push([nx, ny])
            }
        }
    }
    return cnt
}

// 집의 수를 관리할 array
let lst = [];

// 순차적으로 탐색하면서 집이 있거나 아직 방문하지 않은 곳 dfs
for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
        if (guidance[i][j] === "1" && !visited[i][j]) {
            // 결과 바로 array에 push
            let home = dfs(i, j);
            lst.push(home);
        }
    }
}

// 오름차순으로 정렬해서 출력해야함
lst.sort((a, b) => a - b);

// 단지수
console.log(lst.length);

// 단지에 속하는 집의 수
for (home of lst) {
    console.log(home);
}