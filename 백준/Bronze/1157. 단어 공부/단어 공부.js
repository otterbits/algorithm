const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
// default로 대문자로 출력해야하니까
const string = fs.readFileSync(filePath).toString().toUpperCase().trim();
// 알파벳은 26개 있음, index 1을 첫번째 index로 설정
const count = Array.from({length: 27}, () => 0);

for (let i = 0; i < string.length; i++) {
    // 첫번째 문자인 A는 아스키 코드 65이기 때문에 -64를 하면 index = 1
    count[string.charCodeAt(i) - 64] ++;
}

const max = Math.max(...count);
const maxIndex = count.indexOf(max);
// index가 같을 때 boolean으로 판별해줄 변수 지정
let isSame = false;

for (let j = 0; j < count.length; j++) {
    // count가 최대횟수와 같은데, 인덱스가 다르다면 (최댓값인 알파벳이 2개 이상이라면)
    if(count[j] === max && maxIndex != j) {
        // 최댓값인 알파벳이 여러 개다.
        isSame = true;
        break
    }
}

console.log(isSame ? "?" : String.fromCharCode(maxIndex + 64));