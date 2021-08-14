```py

1. 투포인터는 보통 최적의 해를 갖는 연속된 특정 구간을 찾는 문제에서 많이 사용함.

-> 현대카드 4번 문제도 '연속'된 구간 이므로 투포인터 적용 가능

2. 슬라이딩 윈도우는 구간이 정해져있을 때 사용 가능

3. 투포인터 정석 오브 정석
```

```js
function sol(m, arr) {
  let lt = 0;
  let rt = 0;
  let sum = arr[lt];
  let cnt = 0;

  while (rt < arr.length) {
    if (sum === m) {
      cnt++;
      sum -= arr[lt++];
    } else if (sum > m) {
      sum -= arr[lt++];
    } else {
      sum += arr[++rt];
    }
  }
  return cnt;
}
```
