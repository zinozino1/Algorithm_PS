// 11. A를 #으로

function sol(str) {
  let res = "";
  res = str.replace(/A|N/g, "#"); // A and N 을 #으로 바꿔라
  return res;
}

console.log(sol("BANANA"));

// str.replace는 기본적으로 맨앞에 하나만 바꾼다
// 전역적으로 바꾸려면 정규표현식 사용해야함
// str은 immutable
