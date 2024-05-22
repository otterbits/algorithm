const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt"
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const num = input.shift();

for (let i = 0; i < input.length; i += 3) {
    let cmd = input[i]
    let arr = JSON.parse(input[i + 2])
    // 명령어에 R이 많을수록 reverse() 명령어를 계속 실행해야하니, 변수를 통해 제일 마지막에만 뒤바꿔주면 된다.
    let isReverse = false;
    // 에러도 마찬가지로 관리하기 쉽게 변수로 할당해주었다.
    let isError = false;

    for (let nowCmd of cmd) {
        if (nowCmd === "R") {
            // R을 입력 받으면 isReverse의 boolean값을 뒤바꿔준다.
            isReverse = !isReverse;
        } else if (nowCmd === "D") {
            // arr이 없는데 delete를 하면 error니 break한다.
            // 추가 명령어가 없으니 더 이상 R, D의 명령어를 볼 필요가 없다.
            if (arr.length === 0) {
                isError = true;
                break
            }
            // Reverse면 뒤에서 꺼내고, 아니면 앞에서 꺼낸다.
            isReverse ? arr.pop() : arr.shift()
        }
    }
    // 에러면 error 출력, Reverse의 상태에 따라 arr의 순서를 변경하여 출력한다.
    console.log(isError ? "error" : JSON.stringify(isReverse ? arr.reverse() : arr))
}