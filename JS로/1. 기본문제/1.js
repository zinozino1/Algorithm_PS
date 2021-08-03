// 1. 세 수 중 최소값

function sol(arr) {
  let min = 1e9;
  for (let i = 0; i < arr.length; i++) {
    min = Math.min(min, arr[i]);
  }
  return min;
}

console.log(sol([6, 5, 11]));
