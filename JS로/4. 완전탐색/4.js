function sol(n, m, arr) {
  let max = -Infinity;
  for (let i = 0; i < 2; i++) {
    let [p, d] = arr[i];
    if (i == 0) {
      p = parseInt(p / 2);
    }
    let sum = p + d;
    let cnt = 1;
    for (let j = 0; j < n; j++) {
      if (i !== j) {
        if (sum > m) {
          break;
        }
        sum += arr[j][0] + arr[j][1];
        cnt += 1;
      }
    }
    max = Math.max(cnt, max);
  }

  return max;
}

console.log(
  sol(5, 28, [
    [6, 6],
    [2, 2],
    [4, 3],
    [4, 5],
    [10, 3],
  ]),
); // 4
