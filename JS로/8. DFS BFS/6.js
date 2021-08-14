function sol(s, e) {
  let visited = [];
  visited.push(s);
  let q = [s];
  let level = 0;
  while (q.length) {
    for (let _ of q) {
      let curr = q.shift();
      if (curr === e) {
        return level + 1;
      }
      for (let next of [curr + 1, curr - 1, curr + 5]) {
        if (!visited.includes(next)) {
          visited.push(next);
          q.push(next);
        }
      }
    }
    level++;
  }
  return -1;
}

console.log(sol(5, 14));
console.log(sol(8, 3));
