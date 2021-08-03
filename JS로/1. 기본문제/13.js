// 13. 대문자 찾기

// 문자열을 기본적으로 원본 변형 x
function sol(str) {
  for (let s of str) {
    console.log(s.charCodeAt()); // 아스키 코드

    if (s === s.toUpperCase()) {
      // 대문자
      console.log("대문자", s);
    } else if (s === s.toLowerCase()) {
      // 소문자
      console.log("소문자", s);
    }
  }
}

console.log(sol("KoreanIsFuck"));
