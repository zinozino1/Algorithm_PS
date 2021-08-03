// 2. 보이는 학생

function sol(arr) {
  let res = [arr[0]];
  let max = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max) {
      max = arr[i];
      res.push(arr[i]);
    }
  }
  return res.length;
}

console.log(sol([130, 135, 148, 140, 145, 150, 150, 153]));
