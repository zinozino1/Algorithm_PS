function sol(str) {
  let res = "";
  for (let s of str) {
    res += s.charCodeAt() <= 57 && s.charCodeAt() >= 49 ? s : "";
  }

  return res;
}

console.log(sol("1abae32gdsfawf9"));
