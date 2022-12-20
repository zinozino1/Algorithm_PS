// Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".

// Example 1:

// Input: strs = ["flower","flow","flight"]
// Output: "fl"
// Example 2:

// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.

// Constraints:

// 1 <= strs.length <= 200
// 0 <= strs[i].length <= 200
// strs[i] consists of only lowercase English letters.

/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
    let scnt = Infinity;
    for (let str of strs) {
        scnt = Math.min(scnt, str.length);
    }

    let res = "";

    for (let i = 0; i < scnt; i++) {
        let compCh = strs[0][i];

        for (let j = 0; j < strs.length; j++) {
            if (strs[j][i] !== compCh) {
                return res;
            }
        }
        res += compCh;
    }
    return res;
};
