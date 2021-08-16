```js

1. 특정 원소가 배열의 과반수가 넘는지 판별하는 알고리즘

-> 우선 소팅을 한다
-> 만약 과반수가 넘는 원소가 있다면 정렬한 배열의 정 가운데에 필히 그 원소가 있을 것. 과반수가 넘는 원소가 없으면 카운터가 과반수를 넘을 수가 없다.
-> 그 수를 후보로 잡고 카운팅을 돌리면 된다.

function solution(A) {
  // write your code in JavaScript (Node.js 8.9.4)

  let n = A.length;
  let tmp = A.slice();
  tmp.sort((a, b) => a - b);
  let candi = tmp[parseInt(n / 2)];

  let cnt = 0;
  for (let i = 0; i < n; i++) {
    if (A[i] === candi) {
      ++cnt;
      if (cnt >= parseInt(n / 2)) {
        return i;
      }
    }
  }
  return -1;
}





```
