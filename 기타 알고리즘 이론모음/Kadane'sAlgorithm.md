```js

1. 배열에서 최대 부분구간합을 구하는 문제

-> 다이나믹 프로그래밍을 적용한 방식
-> 그냥 dp다 절대 투포인터 x

let arr = [1,-2,3,5,-4,2,5]
-> 답 : [3,5,-4,2,5]

function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    let dp = Array.from({length:A.length}, () => 0)
    dp[0] = A[0]
    for(let i = 1; i < A.length;i++){
        dp[i] = Math.max(dp[i-1]+A[i], A[i])
    }
    return Math.max(...dp)
}

```
