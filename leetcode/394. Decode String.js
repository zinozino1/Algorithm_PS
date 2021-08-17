/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function (s) {
  let stack = [];

  const isNumPattern = /[0-9]/g;
  for (let v of s) {
    if (v === "]") {
      let tmp = "";
      while (stack.length && !isNumPattern.test(stack[stack.length - 1])) {
        const isAlphaPattern = /[a-z]/g;
        let curr = stack.pop();
        if (isAlphaPattern.test(curr)) {
          tmp += curr;
        }
      }

      let num = "";
      while (stack.length && !isNaN(stack[stack.length - 1])) {
        num += stack.pop();
      }
      num = Array.from(num).reverse().join("");

      for (let i = 0; i < parseInt(num); i++) {
        for (let t of Array.from(tmp).reverse().join("")) {
          stack.push(t);
        }
      }
    } else {
      stack.push(v);
    }
  }
  return stack.join("");
};
