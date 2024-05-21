const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "run/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [city, road] = input[0].split(" ").map(Number);
const edges = input.slice(1, road + 1).map((v) => v.split(" ").map(Number));
const num = input[road + 1]
const friends = input[road + 2].split(" ").map(Number);

const graph = Array.from({length: city + 1 }, () => Array(city + 1).fill(Infinity));
let answer = [];
for (let i = 1; i < city; i++) {
    graph[i][i] = 0;
}

edges.forEach(([s, e, w]) => {
    graph[s][e] = w;
});

for (let w = 1; w <= city; w++ ){
    for (let s = 1; s <= city; s++) {
        for (let e = 1; e <= city; e++) {
            graph[s][e] = Math.min(graph[s][e], graph[s][w] + graph[w][e]);
        }
    }
}

const cities = Array(city + 1).fill(0);
for (let x = 1; x <= city; x++) {
    let maxValue = 0;
    for (let friend of friends) {
        if (friend === x || graph[friend][x] === Infinity || graph[x][friend] === Infinity) continue
        maxValue = Math.max(maxValue, graph[x][friend] + graph[friend][x]);
    }
    cities[x] = maxValue;
}

let target = Math.min(...cities.slice(1));
for (let x = 1; x <= city; x++) {
    if ( cities[x] === target ) {
        answer.push(x)
    }
}

console.log(answer.join(" "))