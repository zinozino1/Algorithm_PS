/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function (s, t) {
  let index = 0;
  for (let i = 0; i < s.length; i++) {
    let flag = false;
    for (let j = index; j < t.length; j++) {
      if (t[j] === s[i]) {
        index = j + 1;
        flag = true;
        break;
      }
    }
    if (!flag) {
      return false;
    }
  }
  return true;
};
