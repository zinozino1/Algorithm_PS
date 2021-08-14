function sol(arr) {
  let res = [];
  let max = -Infinity;
  for (let v of arr) {
    let tmp = "" + v;
    let sum = 0;
    for (let t of tmp) {
      sum += parseInt(t);
    }
    if (sum >= max) {
      max = sum;
      res.push([sum, v]);
    }
  }
  res.sort((a, b) => (b[1] === a[1] ? b[0] - a[0] : b[1] - a[1]));
  return res[0][1];
}

function sol2(arr) {
  let max = -Infinity;
  let res = 0;
  for (let v of arr) {
    let sum = Array.from("" + v).reduce((a, v) => a + parseInt(v), 0);
    if (sum > max) {
      max = sum;
      res = v;
    } else if (sum === max) {
      if (v > res) {
        res = v;
      }
    }
  }
  return res;
}

console.log(sol([128, 821, 460, 603, 40, 521, 235, 137, 12345, 123, 54321]));
console.log(sol2([128, 821, 460, 603, 40, 521, 235, 137, 12345, 123, 54321]));
