// 10. 일곱난쟁이

function sol(arr) {
  let final = [];
  let res = [];

  function dfs(L, s, tot) {
    // inner function으로 해야함
    if (L === 7) {
      if (tot === 100) {
        final = res.slice(); // 1차원 배열 복사
      }
      return;
    } else {
      for (let i = s; i < arr.length; i++) {
        res.push(arr[i]);
        dfs(L + 1, i + 1, tot + arr[i]);
        res.pop();
      }
    }
  }

  dfs(0, 0, 0);
  return final;
}

console.log(sol([20, 7, 23, 19, 10, 15, 25, 8, 13]));

// reduce 활용
console.log([1, 2, 3].reduce((c, v, i) => c + v));

// 객체 깊은 복사
let obj = {
  a: 1,
  b: [1, 2, 3],
};

let obj2 = null;
obj2 = JSON.parse(JSON.stringify(obj));
console.log(obj2);

// 배열 깊은 복사
let arr1 = [
  [1, 2, 3],
  [4, 5, 6],
];

let arr2;
arr2 = JSON.parse(JSON.stringify(arr1));
arr1[0][1] = 10;
console.log(arr2);
