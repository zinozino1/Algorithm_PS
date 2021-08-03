// 6. 격자판 최대합

function sol(arr) {
  let max = -Infinity;
  for (let i = 0; i < arr.length; i++) {
    let tmp = 0;
    for (let j = 0; j < arr[i].length; j++) {
      tmp += arr[i][j];
    }
    max = Math.max(max, tmp);
  }
  for (let i = 0; i < arr[0].length; i++) {
    let tmp = 0;
    for (let j = 0; j < arr.length; j++) {
      tmp += arr[j][i];
    }
    max = Math.max(max, tmp);
  }
  return max;
}

console.log(
  sol([
    [10, 13, 10, 12, 15],
    [12, 39, 30, 23, 11],
    [11, 25, 50, 53, 15],
    [19, 27, 29, 37, 27],
    [19, 13, 30, 13, 19],
  ]),
);
