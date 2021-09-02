/**
 * @param {string} s
 * @param {number[]} indices
 * @return {string}
 */
var restoreString = function (s, indices) {
  let beforeSorted = [];
  for (let i = 0; i < s.length; i++) {
    beforeSorted.push([s[i], indices[i]]);
  }

  beforeSorted.sort((a, b) => a[1] - b[1]);
  let res = "";
  beforeSorted.forEach((v) => {
    res += v[0];
  });
  return res;
};
