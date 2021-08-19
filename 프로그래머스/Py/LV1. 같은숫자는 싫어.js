function solution(arr) {
  let res = [arr[0]];
  let prev = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] !== prev) {
      res.push(arr[i]);
    }
    prev = arr[i];
  }
  return res;
}
