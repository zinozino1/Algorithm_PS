// 4. 누적합 구하기

function sol(n) {
  let sum = 0;
  for (let i = 1; i < n + 1; i++) {
    sum += i;
  }
  return sum;
}

console.log(sol(40));

// 같은 값으로 배열 채우기
let arr = new Array(30).fill(0); // [0,0,0]...
// 계산된 수 채우기
let arr2 = Array.from(new Array(30), (v, i) => i); // [0,1,2,3..]
let arr3 = Array.from(new Array(30), (v, i) => i * 2); // [0,2,4,6...]
