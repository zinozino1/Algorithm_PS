// 6. 내장함수로 최소값 최대값 구하기

function sol(arr) {
  return Math.min(...arr);
}

console.log(sol([1, 2, 5, 3, 2, 10, 2, 44, -29]));

// 배열 최대값 최소값 쉽게 구하기 - 스프레드 연산자
let arr = [5, 3, 7, 11, 2, 15, 17];
console.log(Math.min(...arr));
console.log(Math.max(...arr));

// Math.min, Math.max는 낱개로 밖에 들어가지 못한다 .
