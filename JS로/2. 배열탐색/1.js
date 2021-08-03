// 1. 큰 수 출력하기

function sol(arr) {
  let res = [arr[0]];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > arr[i - 1]) {
      res.push(arr[i]);
    }
  }
  return res.join(" "); // 배열을 출력하기
}

console.log(sol([7, 3, 9, 5, 6, 12]));
