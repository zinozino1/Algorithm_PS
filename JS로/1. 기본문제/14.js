// 14. 대문자로 통일

function sol(str) {
  // return str.toUpperCase(); // 메서드 활용

  let res = "";
  for (let s of str) {
    // 이터레이션 활용
    if (s === s.toLowerCase()) {
      res += s.toUpperCase();
    } else {
      res += s;
    }
  }
  return res;
}

console.log(sol("AdsfbaASDfsss"));
