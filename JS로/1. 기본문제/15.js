// 15. 가장 긴 문자열

function sol(arr) {
  let maxLen = -Infinity;
  for (let v of arr) {
    maxLen = Math.max(v.length, maxLen);
  }
  return maxLen;
}

console.log(sol(["teacher", "time", "student", "beautiful", "good"]));
