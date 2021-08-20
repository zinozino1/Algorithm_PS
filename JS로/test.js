let str = "123abcA!@#.....%";

// 1. 숫자를 변경
let str2 = str;
str2 = str2.replace(/[0-9]/g, "n");
console.log(str2);

// 2. 알파벳을 변경
let str3 = str;
str3 = str3.replace(/[a-zA-Z]/g, "=");
console.log(str3);

// 3. 특수문자를 제거
let str4 = str;
let alNum = "1234567890zxcvbnmlkjhgfdsaqwertyuiopAZXSDCVFGBNHJMKLPOIUYTREWQ";
let tmp = "";
for (let s of str4) {
  if (alNum.indexOf(s) !== -1) {
    tmp += s;
  }
}
console.log(tmp);

// 4. "." 중복 제거
let str5 = str;
while (str5.indexOf("..") !== -1) {
  str5 = str5.replace("..", ".");
}
console.log(str5);

// 5. 특정 문자를 특정 문자로 치환
let str6 = str;
let target = "%";
let pattern = new RegExp(`${target}`, "g");
str6 = str6.replace(pattern, "0000");
console.log(str6);
