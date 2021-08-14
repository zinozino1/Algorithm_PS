function sol(arr) {
  let dp = Array.from({ length: arr.length }, () => 0);

  dp[0] = 1;

  for (let i = 1; i < arr.length; i++) {
    let max = -Infinity;
    for (let j = i - 1; j >= 0; j--) {
      if (arr[j] < arr[i]) {
        max = Math.max(max, dp[j]);
      }
    }
    if (max === -Infinity) {
      dp[i] = 1;
    } else {
      dp[i] = max + 1;
    }
  }

  return Math.max(...dp);
}

console.log(sol([5, 3, 7, 8, 6, 2, 9, 4]));
