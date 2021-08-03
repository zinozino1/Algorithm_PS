// 7. 홀수

function sol(arr) {
  // forEach 쓰는 방법

  let min = Infinity;
  let sum = 0,
    ans = [];
  arr.forEach((v, i) => {
    if (v % 2 === 1) {
      sum += v;
      min = Math.min(min, v);
    }
  });
  ans.push(sum, min);
  for (let v of ans) {
    console.log(v);
  }
  // console.log(sum);

  // for...of 쓰는 방법
  // for (let v of arr) {
  //   v % 2 === 1 ? (min = Math.min(min, v)) : min;
  // }

  return min;
}

console.log(sol([12, 77, 38, 41, 53, 92, 85]));
