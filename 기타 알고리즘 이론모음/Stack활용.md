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

```py

2. stack에 값을 넣지 않고 인덱스를 넣는 경우

-> arr = [73, 74, 75 ,71, 69, 72, 76, 73]
-> 각 원소보다 큰 가장 가까운 값과의 인덱스 차이는?
-> res = [1, 1, 4, 2, 1, 1, 0, 0]

-> 스택에 값을 넣는 것이 아니라 인덱스를 넣는다.
-> 스택에 값을 넣기 전 해당 원소보다 작은 값들을 'arr' 에서 판단하고 인덱스를 stack top과 뺀 값이 정답이다.
-> 스택에서 대소를 판단하는 것이 아니라 arr 타겟 배열에서 대소를 판단하는 것이 중요

        stack = []
        res = [0]*len(arr)
        for i, cur in enumerate(arr):
            while stack and cur > arr[stack[-1]]:
                pop = stack.pop()
                res[pop] = i-pop
            stack.append(i)

        return res
```
