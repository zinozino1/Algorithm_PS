/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function (nums) {
  let res = [];

  function dfs(L, arr) {
    if (L === nums.length) {
      res.push(arr.slice());
      return;
    } else {
      arr.push(nums[L]);
      dfs(L + 1, arr);
      arr.pop();
      dfs(L + 1, arr);
    }
  }

  dfs(0, []);
  return res;
};
