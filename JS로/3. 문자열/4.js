function sol(str, target) {
  let arr = Array.from({ length: str.length }, () => 0);

  for (let i = 0; i < str.length; i++) {
    let min = Infinity;
    for (let j = 0; j < str.length; j++) {
      if (str[j] === target) {
        min = Math.min(Math.abs(i - j), min);
      }
    }
    arr[i] = min;
  }

  return arr;
}

console.log(sol("teachemode", "e"));
