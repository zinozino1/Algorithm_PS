// You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by an array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

// The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.

// Write a function:

// function solution(H);

// that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.

// For example, given array H containing N = 9 integers:

//   H[0] = 8    H[1] = 8    H[2] = 5
//   H[3] = 7    H[4] = 9    H[5] = 8
//   H[6] = 7    H[7] = 4    H[8] = 8
// the function should return 7. The figure shows one possible arrangement of seven blocks.

// Write an efficient algorithm for the following assumptions:

// N is an integer within the range [1..100,000];
// each element of array H is an integer within the range [1..1,000,000,000].

function solution(H) {
  // write your code in JavaScript (Node.js 8.9.4)
  let stack = [];
  let cnt = 0;
  for (let i = 0; i < H.length; i++) {
    // 자신보다 큰것들 스택에서 제거
    while (stack.length && stack[stack.length - 1] > H[i]) {
      stack.pop();
    }
    // 처음에 스택이 비었거나 스택 탑이 자신보다 작은 경우
    // 스택 탑이 자신과 같은 경우는 넣지 않고 카운트하지 않는다.
    if (!stack.length || stack[stack.length - 1] < H[i]) {
      stack.push(H[i]);
      cnt++;
    }
  }
  return cnt;
}
