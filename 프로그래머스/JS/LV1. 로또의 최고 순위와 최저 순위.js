// 해시
// reduce 활용

function solution(lottos, win_nums) {
  let zeroCnt = lottos.reduce((a, v) => a + (v === 0 ? 1 : 0), 0);
  let trueCnt = lottos.reduce((a, v) => a + (win_nums.includes(v) ? 1 : 0), 0);
  let tmp = [6, 6, 5, 4, 3, 2, 1];
  return [tmp[zeroCnt + trueCnt], tmp[trueCnt]];
}
