function sol(m, arr) {
  let lt = 0;
  let rt = 0;
  let sum = arr[lt];
  let cnt = 0;

  while (rt < arr.length) {
    if (sum <= m) {
      cnt += rt - lt + 1;
      sum += arr[++rt];
    } else {
      sum -= arr[lt++];
    }
  }

  return cnt;
}

console.log(sol(5, [1, 3, 1, 2, 3]));
