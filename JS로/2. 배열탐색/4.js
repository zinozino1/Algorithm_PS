// 4. 점수 계산

function sol(arr) {
  let res = new Array(arr.length).fill(0);
  let cnt = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === 1) {
      cnt++;
      res[i] = cnt;
    } else {
      cnt = 0;
    }
  }
  return res;
  console.log(cnt);
}

console.log(sol([1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1]));
