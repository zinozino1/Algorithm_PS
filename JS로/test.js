// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(N) {
  // write your code in JavaScript (Node.js 8.9.4)
  console.log(N);

  function getBin(num) {
    let tmp = "";
    while (num !== 1) {
      num = Math.floor(num / 2);
      tmp += num % 2;
    }

    return Array.from(tmp).reverse().join("");
  }

  let res = getBin(N);
  console.log(res);
  let prev = 0; // index
  let cnt = 0;
  let max = -Infinity;
  for (let i = 1; i < res.length; i++) {
    cnt++;
    if (res[i] == "1") {
      prev = i;
      max = Math.max(max, cnt);
      cnt = 0;
    }
  }
  return max === -Infinity ? 0 : max - 1;
}

solution(9);
