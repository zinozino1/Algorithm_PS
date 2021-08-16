```js

1. stack 활용 블록 쌓기


    |
||  ||  |
|| |||| |
|| |||| |
||||||| |
|||||||||
|||||||||
|||||||||
|||||||||
885798748

function solution(H) {
  // write your code in JavaScript (Node.js 8.9.4)
  let stack = [];
  let cnt = 0;
  for (let i = 0; i < H.length; i++) {
    // 자신보다 큰것들 스택에서 제거
    // 자신보다 작거나 같은 애들만 살려야한다. -> 추가되는 높이를 갱신해야되기 때문
    while (stack.length && stack[stack.length - 1] > H[i]) {
      stack.pop();
    }
    // 처음에 스택이 비었거나 스택 탑이 자신보다 작은 경우
    // 스택 탑이 자신과 같은 경우는 넣지 않고 카운트하지 않는다.
    // -> 중복된 영역이기 때문
    if (!stack.length || stack[stack.length - 1] < H[i]) {
      stack.push(H[i]);
      cnt++;
    }
  }
  return cnt;
}




```
