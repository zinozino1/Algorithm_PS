function solution(record) {
  let ans = [];

  let set = {};
  for (let re of record) {
    let [order, id, name] = re.split(" ");
    if (name) {
      set[id] = name;
    }
  }

  for (let re of record) {
    let [order, id, name] = re.split(" ");
    if (order === "Enter") {
      ans.push(`${set[id]}님이 들어왔습니다.`);
    } else if (order === "Leave") {
      ans.push(`${set[id]}님이 나갔습니다.`);
    }
  }

  return ans;
}
