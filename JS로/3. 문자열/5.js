function sol(str) {
  let prev = str[0];
  let cnt = 1;
  let res = "";
  for (let i = 1; i < str.length; i++) {
    if (prev === str[i]) {
      cnt++;
    } else {
      res += prev;
      if (cnt !== 1) {
        res += cnt;
      }
      cnt = 1;
    }

    prev = str[i];
  }
  if (cnt !== 0) {
    res += str[str.length - 1];
    res += cnt;
  }
  return res;
}

console.log(sol("KHSSSSSSHHAAB"));
console.log(sol("KHSSSSSSHHAA"));
console.log(sol("KHSSSSSSHHAABBBBBCCC"));
