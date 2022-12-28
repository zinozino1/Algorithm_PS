// Given two binary strings a and b, return their sum as a binary string.

// Example 1:

// Input: a = "11", b = "1"
// Output: "100"
// Example 2:

// Input: a = "1010", b = "1011"
// Output: "10101"

// Constraints:

// 1 <= a.length, b.length <= 104
// a and b consist only of '0' or '1' characters.
// Each string does not contain leading zeros except for the zero itself.

// BigInt 영역에서는 작동 x이나 문제의 본질은 이게 맞음

/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function (a, b) {
    function decToBin(target) {
        let res = 0;
        for (let i = 0; i < target.length; i++) {
            if (target[i] == "1") {
                res += Math.pow(2, target.length - i - 1); // 제곱승 나타낼 땐 Math.pow
            }
        }
        return res;
    }

    function binToDec(target) {
        if (target == 1) return "1";
        let res = "";
        while (target > 1) {
            res += target % 2;
            target = parseInt(target / 2); // 몫 구할 땐 parseInt해준다
        }

        return target + res.split("").reverse().join("");
    }

    return binToDec(decToBin(a) + decToBin(b));
};
