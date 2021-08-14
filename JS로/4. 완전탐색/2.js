function isPrime(num) {
  let flag = true;
  for (let i = 2; i < num; i++) {
    if (num % i == 0) {
      flag = false;
    }
  }
  return flag;
}

function sol(arr) {
  let res = [];
  for (let v of arr) {
    let tmp = parseInt(Array.from(v.toString()).reverse().join(""));
    if (isPrime(tmp)) {
      res.push(tmp);
    }
  }
  return res;
}

console.log(sol([32, 55, 62, 20, 250, 370, 200, 30]));
