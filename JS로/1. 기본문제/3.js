// 3. 연필개수

function sol(n) {
  let answer;
  answer = n / 12;

  return Math.ceil(answer);
}

console.log(sol(23));

// Math.ceil : 2.111 -> 3 (올림)
// Math.floor : 2.555 -> 2 (버림)
// Math.round : 2.5 -> 3 (반올림)
