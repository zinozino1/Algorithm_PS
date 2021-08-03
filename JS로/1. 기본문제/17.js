// 17. 중복문자제거

function sol(str) {
  //  set 이용
  let set = new Set();
  for (let v of str) {
    console.log(v);
    set.add(v);
  }
  return [...set].join("");
}

console.log(sol("ksekkseksabd"));

// 문자열을 배열로 변경
let arr = Array.from("abcd");
console.log(arr);
