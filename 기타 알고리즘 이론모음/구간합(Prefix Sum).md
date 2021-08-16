```js


* 구간 합 알고리즘

-> 일반적인 방법으로 구간합을 구하면 n^2
-> 미리 sum 배열을 만들어놓으면 n
-> 주의할것은 구간합 a,b를 구할 때 sum[b]-sum[a]가 아니라 sum[b]-sum[a-1]
-> 1번째 인덱스부터 활용해야 하므로 타겟, sum배열 맨 앞에 0 추가시켜준다.



let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];

let sum = Array.from({ length: arr.length }, () => 0);
sum[0] = arr[0];
for (let i = 1; i < arr.length; i++) {
  sum[i] = sum[i - 1] + arr[i];
}
console.log(sum);

// a-b 구간합

console.log(sum[b] - sum[a - 1]);

-> o(N)에 해결 가능
```
