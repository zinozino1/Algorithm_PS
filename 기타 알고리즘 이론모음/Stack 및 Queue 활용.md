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

```js

3. 스택, 큐 구현

class Stack {
  constructor() {
    this.arr = [];
    this.top = -1
  }
  push(val) {
    this.top++;
    this.arr[this.top] = val
  }

  pop() {
    if(this.top > -1){
      return this.arr[this.top--]
    }
    return null
  }

  empty() {
    return this.arr.length === 0;
  }

  peek() {
    return this.arr[this.top]
  }
}

class Queue {
  constructor() {
    this.arr = [];
  }
  enqueue(val) {
    this.arr.push(val);
  }
  dequeue() {
    return this.arr.shift();
  }
  empty() {
    return this.arr[this.arr.length - 1];
  }
  peek() {
    return this.arr[0];
  }
}


```

```js

4. 스택 두개로 큐 하나 만들기

class StackToQueue {
  constructor() {
    this.stack1 = [];
    this.stack2 = [];
  }
  enqueue(val) {
    this.stack1.push(val);
  }

  dequeue() {
    if (this.stack2.length === 0) {
      while (this.stack1.length) {
        this.stack2.push(this.stack1.pop());
      }
    }
    return this.stack2.pop();
  }
  size() {
    return this.stack1.length + this.stack2.length;
  }
}




```

```js

5. 큐 하나로 스택 만들기


class QueueToStack {
  constructor() {
    this.q = [];
  }
  push(val) {
    for (let i = 0; i < this.q.length - 1; i++) {
      this.q.push(this.q.unshift());
    }
  }
  pop() {
    return this.q.shift();
  }
  peek() {
    return this.arr[0];
  }
}



```
