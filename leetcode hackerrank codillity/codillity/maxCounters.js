function solution(N, A) {
  // 0으로 초기화된 길이 N의 배열을 만든다.
  const array = Array(N).fill(0);
  // 배열 내 최대 값
  let max = 0;
  // 마지막 max counter의 기준이 되었던 수
  let maxCounter = 0;
  for (let i = 0; i < A.length; i++) {
    // 모든 숫자를 올려야 하는 경우
    if (A[i] > N) {
      // maxCounter에 다같이 올라가는 최대 숫자를 저장해 둔다.
      maxCounter = max;

      // 하나씩만 올리면 되는 경우
    } else {
      // 현재 숫자가 maxCounter보다 작을 경우 maxCounter로 초기화 한다.
      if (array[A[i] - 1] < maxCounter) {
        array[A[i] - 1] = maxCounter;
      }

      // 그리고 +1을 한다
      array[A[i] - 1] += 1;

      // 이렇게 새롭게 세팅된 숫자가 배열의 최대값인지 확인한다.
      if (max < array[A[i] - 1]) {
        max = array[A[i] - 1];
      }
    }
  }

  // 배열의 값이 maxCounter보다 작다면 그 값으로 리턴한다.
  return array.map((i) => (i < maxCounter ? maxCounter : i));
}
