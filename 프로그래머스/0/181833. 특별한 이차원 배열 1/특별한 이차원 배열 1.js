function solution(n) {
    // 빈배열 생성 후 모든 요소를 0으로 채움
    const arr = Array.from(Array(n), () => Array(n).fill(0));
    
    for (let i = 0 ; i < n; i++) {
        arr[i][i] = 1
    }

    return arr
}