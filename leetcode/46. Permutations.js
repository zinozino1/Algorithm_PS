/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function (nums) {
  let check = Array.from({ length: nums.length }, () => 0);
  let res = [];

  function dfs(L, arr) {
    if (L === nums.length) {
      res.push(arr.slice());
      return;
    } else {
      for (let i = 0; i < nums.length; i++) {
        if (check[i] == 0) {
          check[i] = 1;
          arr.push(nums[i]);
          dfs(L + 1, arr);
          check[i] = 0;
          arr.pop();
        }
      }
    }
  }

  dfs(0, []);

  return res;
};
