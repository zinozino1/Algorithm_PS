// function sol(m, arr) {
//   let lt = 0;
//   let rt = 0;
//   let sum = 0;
//   let cnt = 0;
//   while (true) {
//     // console.log(lt, rt, sum, cnt);
//     if (rt > arr.length || lt > arr.length) {
//       break;
//     }
//     if (sum === m) {
//       sum -= arr[lt];
//       cnt++;
//       lt++;
//     } else if (sum > m) {
//       sum -= arr[lt];
//       lt++;
//     } else {
//       sum += arr[rt];
//       rt++;
//     }
//   }
//   if (sum == m) {
//     cnt++;
//   }
//   return cnt;
// }

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

// console.log(sol(6, [1, 2, 1, 3, 1, 1, 1, 2]));
// console.log(sol(5, [1, 2, 3, 1, 2, 3, 1, 2, 33, 4, 1]));
// console.log(sol(4, [1, 1, 1, 1, 1, 1, 1, 1, 2]));
console.log(sol(3, [1, 1, 1, 1]));
