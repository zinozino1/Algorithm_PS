// 2. 삼각형 판별하기

function sol(a, b, c) {
  let arr = [a, b, c];

  arr.sort(function (a, b) {
    return a - b;
  });

  return arr[0] + arr[1] > arr[2] ? true : false;
}

console.log(sol(6, 7, 11));
