function sol(str) {
  return str.toUpperCase() === Array.from(str.toUpperCase()).reverse().join("")
    ? "YES"
    : "NO";
}

console.log(sol("Goooddd"));
console.log(sol("Goog"));
console.log(sol("ddd"));
