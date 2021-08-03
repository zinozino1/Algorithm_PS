// 3. 가위바위보

function sol(a, b) {
  let res = [];
  for (let i = 0; i < a.length; i++) {
    if (a[i] - b[i] < 0) {
      if (a[i] === 1 && b[i] === 3) {
        res.push("A");
      } else {
        res.push("B");
      }
    } else if (a[i] - b[i] > 0) {
      if (a[i] === 3 && b[i] === 1) {
        res.push("B");
      } else {
        res.push("A");
      }
    } else {
      res.push("D");
    }
  }
  res.forEach((v, i) => {
    console.log(v);
  });
  return res;
}

console.log(sol([2, 3, 3, 1, 3], [1, 1, 2, 2, 3]));
