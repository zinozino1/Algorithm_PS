/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function (n, k) {
  let res = [];
  function dfs(L, s, arr) {
    if (L === k) {
      res.push(arr.slice());
      return;
    } else {
      for (let i = s; i < n; i++) {
        arr.push(i + 1);
        dfs(L + 1, i + 1, arr);
        arr.pop();
      }
    }
  }
  dfs(0, 0, []);
  return res;
};
