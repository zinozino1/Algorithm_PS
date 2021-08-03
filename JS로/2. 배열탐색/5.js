// 5. 등수 구하기

function sol(arr) {
  let tmp = [];
  for (let i = 0; i < arr.length; i++) {
    tmp.push([arr[i], i]);
  }

  tmp.sort((x, y) => (x[0] === y[0] ? x[1] - x[1] : y[0] - x[0]));
  for (let i = 0; i < arr.length; i++) {
    tmp[i].push(i);
  }

  tmp.sort((x, y) => x[1] - y[1]);

  tmp.forEach((v) => {
    console.log(v[2] + 1);
  });
}

console.log(sol([87, 89, 92, 100, 76]));

// 객체 배열 초기화
let arr1 = Array.from({ length: 10 }, () => {
  return {};
});
// 이차원 배열 초기화
let arr2 = Array.from({ length: 3 }, () => Array());

// 3차원 배열 초기화
let arr4 = Array.from({ length: 3 }, () =>
  Array.from({ length: 3 }, () => Array(3).fill(0)),
);
console.log(arr4);

let arr3 = [
  [1, 2],
  [3, 4],
  [5, 6],
];
// console.log(Object.fromEntries(arr3));
for (let i = 0; i < arr3.length; i++) {
  let a = arr3[i][0];
  let b = arr3[i][1];
  arr2[i][0] = a;
  arr2[i][1] = b;
}
console.log(arr2);

// 객체 배열 정렬

let arr = [
  { a: 100, b: 30 },
  { a: 30, b: 30 },
  { a: 19, b: 3333 },
];
let item = "b";
console.log(arr);
arr.sort((x, y) => (x.b === y.b ? x.a - y.a : x.b - y.b));
console.log(arr);
