// Given a sorted array of distinct integers and a target value, return the index if the target is found.
// If not, return the index where it would be if it were inserted in order.

// You must write an algorithm with O(log n) runtime complexity.

// Example 1:

// Input: nums = [1,3,5,6], target = 5
// Output: 2
// Example 2:

// Input: nums = [1,3,5,6], target = 2
// Output: 1
// Example 3:

// Input: nums = [1,3,5,6], target = 7
// Output: 4

// Constraints:

// 1 <= nums.length <= 104
// -104 <= nums[i] <= 104
// nums contains distinct values sorted in ascending order.
// -104 <= target <= 104

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function (nums, target) {
    let [lt, rt] = [0, nums.length - 1];
    let res = -1;

    while (lt <= rt) {
        let mid = Math.floor((lt + rt) / 2);

        if (nums[mid] == target) {
            res = mid;
            break;
        } else if (nums[mid] > target) {
            rt = mid - 1;
        } else if (nums[mid] < target) {
            lt = mid + 1;
        }
    }

    return res === -1 ? Math.max(lt, rt) : res;
};

console.log(searchInsert([1, 3, 5, 6], -1));
