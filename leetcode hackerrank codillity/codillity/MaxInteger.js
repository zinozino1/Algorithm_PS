// Write a function:

// function solution(A);

// that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

// For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

// Given A = [1, 2, 3], the function should return 4.

// Given A = [−1, −3], the function should return 1.

// Write an efficient algorithm for the following assumptions:

// N is an integer within the range [1..100,000];
// each element of array A is an integer within the range [−1,000,000..1,000,000].

function solution(A) {
  // write your code in JavaScript (Node.js 8.9.4)
  let set = [...new Set(A)].sort((a, b) => a - b);

  if (set[set.length - 1] < 0) {
    return 1;
  }
  if (set[0] > 0 && set[0] !== 1) {
    return 1;
  }
  if (set.length === 1) {
    if (set[0] === 1) {
      return 2;
    }
    return 1;
  }
  let prev = set[0];
  for (let i = 1; i < set.length; i++) {
    if (set[i - 1] < 0 && set[i] < 0) {
    } else if (set[i - 1] < 0 && set[i] === 0) {
    } else if (set[i - 1] < 0 && set[i] > 0) {
      if (set[i] > 1) {
        return 1;
      }
    } else if (set[i - 1] >= 0 && set[i] >= 0) {
      if (set[i] - prev !== 1) {
        return ++prev;
      }
    }
    prev = set[i];
  }
  return ++set[set.length - 1];
}
