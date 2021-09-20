/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function (candidates, target) {
  // 중복 조합
  let res = [];

  function dfs(L, arr, sum, s) {
    if (sum >= target) {
      if (sum === target) {
        res.push(arr.slice());
      }
      return;
    }

    for (let i = s; i < candidates.length; i++) {
      arr.push(candidates[i]);
      dfs(L, arr, sum + candidates[i], i);
      arr.pop();
    }
  }

  dfs(0, [], 0, 0);
  return res;
};
