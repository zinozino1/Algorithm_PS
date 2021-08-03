// 16. 가운데 문자 출력

function sol(str) {
  let index = Math.floor(str.length / 2);
  if (str.length % 2 !== 0) {
    console.log(str[index]);
  } else {
    console.log(str.substring(index - 1, index + 1));
  }
}

console.log(sol("assc"));
let s = "123";
console.log(parseInt(s)); // 문지열을 숫자로 변경

let str2 = "abcdefg";

console.log(str2.substring(0, 2)); // index를 알 때
console.log(str2.substr(0, 2)); // index를 모를 때
