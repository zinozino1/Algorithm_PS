function solution(numbers, hand) {
  let keyPad = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2],
    "*": [3, 0],
    0: [3, 1],
    "#": [3, 2],
  };

  let leftPos = [3, 0];
  let rightPos = [3, 2];
  let res = "";
  for (let number of numbers) {
    let target = number + "";
    if (target === "1" || target === "4" || target === "7") {
      res += "L";
      leftPos = keyPad[target];
    } else if (target === "3" || target === "6" || target === "9") {
      res += "R";
      rightPos = keyPad[target];
    } else {
      let leftDis =
        Math.abs(leftPos[0] - keyPad[target][0]) +
        Math.abs(leftPos[1] - keyPad[target][1]);
      let rightDis =
        Math.abs(rightPos[0] - keyPad[target][0]) +
        Math.abs(rightPos[1] - keyPad[target][1]);
      if (leftDis < rightDis) {
        res += "L";
        leftPos = keyPad[target];
      } else if (leftDis > rightDis) {
        res += "R";
        rightPos = keyPad[target];
      } else {
        if (hand === "right") {
          res += "R";
          rightPos = keyPad[target];
        } else {
          res += "L";
          leftPos = keyPad[target];
        }
      }
    }
  }
  return res;
}
