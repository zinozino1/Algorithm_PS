// 문자열
// slice 이용

function solution(s) {
  let min = Infinity;

  for (let i = 1; i <= parseInt(s.length / 2); i++) {
    let tmp = "";
    let prev = s.slice(0, i);
    let cnt = 1;
    for (let j = i; j < s.length; j += i) {
      if (prev === s.slice(j, j + i)) {
        cnt++;
      } else {
        tmp += prev + (cnt === 1 ? "" : cnt);
        cnt = 1;
      }
      prev = s.slice(j, j + i);
    }

    tmp += prev + (cnt === 1 ? "" : cnt);
    min = Math.min(tmp.length, min);
  }

  return s.length === 1 ? 1 : min;
}
