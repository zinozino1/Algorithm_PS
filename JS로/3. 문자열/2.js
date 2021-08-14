function sol(str) {
  let target = str.toUpperCase();
  for (let i = 0; i < Math.ceil(target.length / 2); i++) {
    console.log(target[i]);
  }
  return;
}

console.log(sol("AbAaaBS"));
console.log(sol("AAAA"));
console.log(sol("AbA"));
