const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

// 테스트 케이스 개수
const tc = input.shift();

// 상하좌우 한번 써보기
const directions = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1]
]

// dfs지만, test case가 여러 개기 때문에, 각각 row/col/field/visited를 받아야한다.
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

// test case 개수만큼 탐색
for (let i = 0; i < tc; i++) {

    // 첫째 줄 가로길이, 세로길이, 배추가 심어져 있는 위치의 개수
    let [row, col, locCnt] = input.shift().split(" ");
    // 배추가 심어져 있는 위치의 개수만큼 splice하여 'location'이라는 배추가 심어져 있는 위치 배열 생성
    let location = input.splice(0, locCnt);
    
    // 기본 밭의 정보(어디 심어져있는지, 밭의 2차원 배열, 방문 여부 배열) 갱신
    let field = Array.from({length: col}, () => Array.from({length: row}, () => 0));
    for (loc of location) {
        let [locY, locX] = loc.split(" ").map(Number);
        field[locX][locY] = 1;
    }
    let visited = Array.from({length: col}, () => Array.from({length: row}, () => false));

    // 지렁이 개수
    let cnt = 0;

    // 배추가 심어져 있는 위치 돌기
    for (loc of location) {
        let [locY, locX] = loc.split(" ").map(Number);
        if (!visited[locX][locY]) {
            dfs(locX, locY, row, col, field, visited);
            // dfs하면 지렁이 개수 추가
            cnt ++;
        }
    }

    // test case 한 번 끝날때 마다 지렁이 개수 출력
    console.log(cnt);
}
