const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [n, k] = input[0].split(" ").map(Number);
const seq = input[1].split(" ").map(Number);
// 최장 부분수열의 길이가 100,000만 이므로 그만큼의 숫자 count 배열 만들기
const count = Array.from({length : 100001}, () => 0);

// 최장 연속 부분 수열의 길이 저장
let maxLength = 0;
// 포인터 index
let start = 0;
let end = 0;

// end 포인터가 전체 수열의 길이보다 작을 때까지 탐색
while (end < n) {
    // end 포인터에 배열의 숫자가 k개 이하면, end 포인터를 뒤로 옮기면서 start count 늘려주기
    if (count[seq[end]] < k) {
        count[seq[end]] ++;
        end ++;
    // k개 이상이면, start 포인터를 뒤로 옮기면서 start의 count 줄여주기
    } else {
        count[seq[start]] --;
        start ++;
    }

    // 매번 최대 길이 갱신
    maxLength = Math.max(maxLength, end - start);
}

console.log(maxLength)