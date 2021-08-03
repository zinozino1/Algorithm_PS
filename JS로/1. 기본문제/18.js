// 18. 중복단어 제거

function sol(arr) {
  // set 이용 풀이
  let set = new Set();
  arr.forEach((v, i) => {
    set.add(v);
  });
  return [...set];
}

console.log(sol(["good", "time", "good", "time", "student"]));
