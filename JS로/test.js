let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];

let sum = Array.from({ length: arr.length }, () => 0);
sum[0] = arr[0];
for (let i = 1; i < arr.length; i++) {
  sum[i] = sum[i - 1] + arr[i];
}
console.log(sum);

// a-b 구간합

console.log(sum[b] - sum[a - 1]);
