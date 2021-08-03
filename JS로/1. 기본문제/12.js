// 12. 문자 찾기(특정 문자 카운팅)

function sol(str, target) {
  // 1. 단순 이터레이션
  let ans = 0;
  for (let s of str) {
    if (s === target) {
      ans++;
    }
  }
  return ans;

  // 2. split 활용 -> 타겟 문자 확정되어있지 않을 떄
  let tmp = str.split(target);
  let res = tmp.length - 1;
  console.log(res);

  // 3. match + regex 활용 -> 타겟 문자 확정되어있을 때
  let tmp2 = str.match(/R/g);
  let res2 = tmp2.length;
  console.log(res2);
}

console.log(sol("COMPUTERPROGRAMMING", "R"));
