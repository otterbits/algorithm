function solution(binomial) {
    const [a, op, b] = binomial.split(' ')
    let Num1 = Number(a)
    let Num2 = Number(b)
    
    let result;
    if (op === '+') {
        result = Num1 + Num2
    } else if (op === '-') {
        result = Num1 - Num2
    } else if (op === '*') {
        result = Num1 * Num2
    }
    
    return result
}