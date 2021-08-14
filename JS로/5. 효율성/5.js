function sol(n, str) {
  let obj = {};
  for (let s of str) {
    if (!obj[s]) {
      obj[s] = 1;
    } else {
      obj[s]++;
    }
  }
  let max = -Infinity;
  let res = 0;
  for (let v in obj) {
    if (max < obj[v]) {
      max = obj[v];
      res = v;
    }
  }

  return res;
}

console.log(sol(15, "SSBACBACCACCBDEDE"));
