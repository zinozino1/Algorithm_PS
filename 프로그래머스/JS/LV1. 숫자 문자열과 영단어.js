function solution(s) {
  let number = {
    one: "1",
    two: "2",
    three: "3",
    four: "4",
    five: "5",
    six: "6",
    seven: "7",
    eight: "8",
    nine: "9",
    zero: "0",
  };

  for (let [key, value] of Object.entries(number)) {
    let pattern = new RegExp(`${key}`, "g");
    s = s.replace(pattern, value);
  }
  return parseInt(s);
}
