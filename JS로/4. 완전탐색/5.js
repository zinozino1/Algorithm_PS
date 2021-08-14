function sol(n, k, arr) {
  let res = new Set();
  function dfs(L, s, tot) {
    if (L === 3) {
      res.add(tot);
      return;
    } else {
      for (let i = s; i < arr.length; i++) {
        dfs(L + 1, i + 1, tot + arr[i]);
      }
    }
  }

  dfs(0, 0, 0);

  return Array.from(res).sort((a, b) => b - a)[k - 1];
}

console.log(sol(10, 3, [13, 15, 34, 23, 45, 65, 33, 11, 26, 42]));
