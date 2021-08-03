// 7. 봉우리

function sol(arr) {
  let dx = [0, 1, 0, -1];
  let dy = [1, 0, -1, 0];
  for (let v of arr) {
    v.unshift(0);
    v.push(0);
  }

  arr.unshift(Array.from({ length: arr.length }, () => 0));
  arr.push(Array.from({ length: arr.length }, () => 0));
  console.log(arr);
  let res = 0;
  for (let i = 1; i < arr.length - 1; i++) {
    for (let j = 1; j < arr[i].length - 1; j++) {
      let cnt = 0;
      for (let s = 0; s < 4; s++) {
        let nx = i + dx[s];
        let ny = j + dy[s];
        if (
          nx >= 0 &&
          nx <= arr.length - 1 &&
          ny >= 0 &&
          ny <= arr[i].length - 1 &&
          arr[i][j] > arr[nx][ny]
        ) {
          cnt++;
        }
      }
      if (cnt > 3) {
        console.log(arr[i][j]);
        res += 1;
      }
    }
  }
  return res;
}

console.log(
  sol([
    [5, 3, 7, 2, 3],
    [3, 7, 1, 6, 1],
    [7, 2, 5, 3, 4],
    [4, 3, 6, 4, 1],
    [8, 7, 3, 5, 2],
  ]),
);
