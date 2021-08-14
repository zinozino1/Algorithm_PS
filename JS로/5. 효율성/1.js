// function sol(n, arr1, m, arr2) {
//   let lt = 0,
//     rt = 0;

//   let res = [];
//   while (1) {
//     if (lt > arr1.length - 1) {
//       break;
//     }
//     if (rt > arr2.length - 1) {
//       break;
//     }
//     if (arr1[lt] < arr2[rt]) {
//       res.push(arr1[lt]);
//       lt++;
//     } else if (arr1[lt] > arr2[rt]) {
//       res.push(arr2[rt]);
//       rt++;
//     } else {
//       res.push(arr1[lt]);
//       res.push(arr2[rt]);
//       lt++;
//       rt++;
//     }
//   }

//   if (rt === arr2.length) {
//     res = res.concat(arr1.slice(lt));
//   } else if (lt === arr1.length) {
//     res = res.concat(arr2.slice(rt));
//   }
//   return res.join(" ");
// }

function sol(arr1, arr2) {
  let n = arr1.length,
    m = arr2.length;

  let p1 = 0;
  let p2 = 0;

  let res = [];

  while (p1 < n && p2 < m) {
    if (arr1[p1] < arr2[p2]) {
      res.push(arr1[p1++]);
    } else if (arr1[p1] > arr2[p2]) {
      res.push(arr2[p2++]);
    } else {
      res.push(arr1[p1++]);
      res.push(arr2[p2++]);
    }
  }

  while (p1 < n) {
    res.push(arr1[p1++]);
  }
  while (p2 < m) {
    res.push(arr2[p2++]);
  }

  return res.join(" ");
}

console.log(sol([1, 3, 5], [2, 3, 6, 7, 9]));
