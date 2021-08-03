// 8. 10부제

function sol(n, arr) {
  let ans = 0;
  // for (let v of arr) { // 문자열 이용 풀이
  //   let tmp = "" + v;
  //   ans += tmp[1] === "" + n ? 1 : 0;
  // }

  for (let v of arr) {
    // 나머지 이용 풀이
    if (v % 10 === n) {
      ans++;
    }
  }
  return ans;
}

console.log(sol(3, [25, 23, 11, 47, 53, 17, 33]));
