// 5. 최소값 구하기

function sol(arr) {
  let min = Infinity;
  for (let i = 0; i <= arr.length - 1; i++) {
    min = Math.min(min, arr[i]);
  }
  return min;
}

console.log(sol([5, 3, 7, 11, 2, 15, 17]));
