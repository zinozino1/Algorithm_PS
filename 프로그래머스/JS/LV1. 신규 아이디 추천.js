// 문자열
// 정규표현식 + 문자열 내장 메서드 활용

function solution(new_id) {
  let res = "";

  // 1
  res = new_id.toLowerCase();

  // 2
  let tmp = "";
  for (let s of res) {
    const numPattern = /[0-9]/g;
    const alphaPattern = /[a-zA-Z]/g;
    if (
      numPattern.test(s) ||
      alphaPattern.test(s) ||
      s === "-" ||
      s === "_" ||
      s === "."
    ) {
      tmp += s;
    }
  }
  res = tmp;

  // 3
  while (res.indexOf("..") !== -1) {
    res = res.replace("..", ".");
  }

  // 4
  let tmp2 = "";
  for (let i = 0; i < res.length; i++) {
    if (i == 0 || i === res.length - 1) {
      if (res[i] !== ".") {
        tmp2 += res[i];
      }
    } else {
      tmp2 += res[i];
    }
  }
  res = tmp2;

  // 5
  if (!res.length) {
    res = "a";
  }

  // 6
  if (res.length >= 16) {
    res = res.slice(0, 15);
  }
  if (res[res.length - 1] === ".") {
    res = res.slice(0, res.length - 1);
  }

  // 7
  if (res.length <= 2) {
    let last = res[res.length - 1];
    while (res.length !== 3) {
      res += last;
    }
  }

  return res;
}
