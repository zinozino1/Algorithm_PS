```js



1. 정렬

-> 기본 정렬 되지 않으므로 람다함수 넣어줘야함
-> [3,2,1]
-> arr.sort((a,b) => a-b) // 오름차순
-> arr.sort((a,b) => b-a) // 내림차순

// 2차원 배열은 이렇게
->[[1,2],[2,3],[2,1]]

-> arr.sort((a,b) => (정렬할 자리 ? 반대쪽 자리 : 정렬할 자리))

// 0번째 자리 기준 정렬, 오름차순
-> arr.sort((a, b) => (a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]));
// 1번째 자리 기준 정렬, 내림차순
-> arr.sort((a, b) => (a[1] === b[1] ? b[0] - a[0] : b[1] - a[1]));

// 객체배열도 동일하게 작동
let arr = [
  { a: 100, b: 30 },
  { a: 30, b: 30 },
  { a: 19, b: 3333 },
];

let item = "b";
console.log(arr);
arr.sort((x, y) => (x.b === y.b ? x.a - y.a : x.b - y.b));
// b먼저 그다음 a






2. Math 라이브러리

-> Math.max Math.min -> 개별 값으로 인자가 들어가므로 전개연산자 사용해야함
-> Math.max(...[1,2,3])

// parseInt 말고 이것을 쓸 것
-> Math.ceil : 올림
-> Math.floor : 내림
-> Math.round : 반올림






3. 배열 초기화

[0,0,0,0,...]
-> Array.from({length:n}, ()=>0)
[1,2,3,4,5,6]
-> Array.from({length:n}, (v,i) => i)
[{},{},{}...]
-> Array.from({length:n}, () => {
  return {}
})
[[], [], []...]
-> Array.from({length:n}, () => new Array())



let arr = Array.from({ length: 10 }, () => { // 행
  return Array.from({ length: 4 }, () => 0); // 열
});

for (let a of arr) {
  console.log(a);
}





4. for..of

-> 이터러블 객체에 사용 가능
-> string, arr, set, map...






5. 배열 및 객체 복사

let arr1 = [1,2,3]
-> arr2 = [...arr1] or arr1.slice()

let arr3 = [[1,2,3],[4,5,6]]
-> arr4 = JSON.parse(JSON.stringify(arr3))

let obj = {a:1}
-> obj2 = Object.assign({}, obj) or {...obj}



5.5 문자열 자주 쓰이는 메서드

// String.prototype 메서드는 모두 원본 변경 x tmp를 써야함.

let str = "abc";

str.replace(정규식, 바꿀문자);
str.split(구분할문자);
str.slice(자를시작인덱스, 자를끝인덱스(1더해짐));
str.charAt(인덱스);
str.indexOf(특정문자나문자열);


6. 문자열 특정 값 변경 -> String.prototype 메서드는 기본적으로 원본 변경 x

let str = "ABCDEFFFFF"
-> let tmp = str.replace(/F/g, "#") // ABCDE#####
-> let tmp2 = str.replace(/[a-zA-Z]/g, "#") // #########


or 단순 반복문






7. 문자열에서 문자 카운팅

let tmp2 = str.split("F")
-> let cnt = tmp2.length - 1






8. 대문자, 소문자, 아스키코드

let str = "ABCdacbasS"
for (let s of str) {
  console.log(s.charCodeAt()); // 아스키 코드

  if (s === s.toUpperCase()) {
    // 대문자
    console.log("대문자", s);
  } else if (s === s.toLowerCase()) {
    // 소문자
    console.log("소문자", s);
  }
  }




9. 문자열을 숫자로 변경

let str = "123"
-> let num = parseInt(str)





10. 문자열 슬라이싱

let str = "123,456,789"
-> let p1 = str.slice(0, 3)



10.5 배열 자주 사용하는 메서드

// 원본 변경
arr.push()
arr.pop()
arr.unshift()
arr.shift()
arr.sort()
arr.reverse()

// 원본 변경 x
let res = arr.join(str) // 문자열로
let res = arr.slice(firstIndex,lastIndex) // 배열 자르기
let res = arr.includes(elem) // 원소 포함하는지 - boolean
let res = arr.find(cb) // 콜백함수 만족하는 원소 찾기
let res = arr.indexOf(elem) // 원소 인덱스 위치 -- String 메서드 indexOf도 사용하기 위해 이걸로 통일





11. 배열 원소들 출력

-> let arr = [1,2,3]
# 123
let a1 = arr.join("")
# 1,2,3
let a2 = arr.join(",") // === arr.toString()





11. 배열 첫번쨰자리, 마지막자리 원소 삽입

let arr = [1,2,3]
arr.push(4) // 마지막 자리
arr.unshift(0) // 첫번쨰 자리





12. 딕셔너리 쓰기

let obj = {} 으로 가능

// 테크닉
let arr = [1, 2, 3, 1, 2, 2, 2, 3, 1, 4, 6];

let obj = {};

for (let a of arr) {
    obj[a] = ++obj[a] || 1;
}




13. 문자열 배열 sorting
-> 알파벳순으로 소팅됨




14. 문자열 -> 배열
let str = "abc"
let arr = Array.from(str) // 문자배열

let str2 = "123"
let arr2 = Array.from(str, (s) => parseInt(s)); // 숫자배열



15. 문자열 대문자화

let str = "abc"
let newStr = str.toUpperCase()

let c = "a"
let newC = str.toUpperCase() // 문자 하나도 가능




16. 두 배열이 같은지 확인
if(JSON.stringify([1,2,3]) === JSON.stringify([1,2,3]))





17. 이차원 배열에서 포함되어있는지 확인

let arr2 = [[1,2,3],[4,5,6]]
let target = [1,2,3]

let flag = false;
arr2.forEach((item) => {
  if (JSON.stringify(item) === JSON.stringify(target)) {
    flag = true;
  }
});

console.log(flag);





18. 배열 원소 포함여부 3종 세트

let arr = [[1, 2, 3], 4, 5, 6];
console.log(arr.indexOf([1, 2, 3])); // -1 불가능
console.log(arr.indexOf(4)); // 1
console.log(arr.includes(4)); // true

*******
문자열, 배열 둘 모두 포함 여부를 indexOf === -1 로 판단하자 쉽게 그냥
*******





19. 배열 고차함수 세트

let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];

console.log(arr.filter((v, i) => v > 3));
console.log(arr.map((v, i) => v + 3));
console.log(arr.every((v) => v > 1));
console.log(arr.some((v) => v > 3));
console.log(arr.reduce((a, v, i) => a + v), 0);






20. js 알고리즘 그냥 in 못 쓴다고 보면 된다.





21. 문자열 포함

let str = "aabbccddeeff";

console.log(str.indexOf("a"));
console.log(str.lastIndexOf("a"));
console.log(str[0]);
console.log(str.slice(5)); // 주의 : 5 부터임

// 정규 표현식을 알아야하고, 정규표현식 안에 변수를 넣을 수 없음 ..
str = str.replace(/a/g, "1"); // 재할당은 가능하지 당연
console.log(str);

let char = "a";
let newStr2 = str.replace(char, "1"); // 맨 앞 하나밖에 안바뀜
console.log(newStr2);


// 정규식 쓰지 않고 모든 문자 대체하는 방법
let char2 = "b";
let str2 = "aaaaaaaaa";

while (str2.indexOf("a") !== -1) { // 포함되어 있지 않다를 표현 - 상당히 중요한 테크닉
  str2 = str2.replace("a", char2);
}
console.log(str2);

let str3 = "11jdj891hf"
let res = ''

for(let s of str3){
  if(s.charAtCode()<=...){
    res += s
  }
}

// 숫자만 추출 간단하게.
let str2 = "ab2cwads348adg7df8ag7";

let res = "";
for (let s of str2) {
  if (!isNaN(s)) {
    res += s;
  }
}

console.log(res);

// 정규표현식 이용 특정 문자 대치
let str = "asdb advg$ af333 fasdf #@#%%@#$";

console.log(str.replace(/[0-9]/g, "[]")); // 숫자 대치
console.log(str.replace(/[a-zA-Z]/g, "=")); // 소문자, 대문자 대치
console.log(str.replace(/[a-z]/g, "=")); // 소문자 대치
console.log(str.replace(/[!@#$%]/g, "9")); // !@#$ 특수문자 대치


// 알파벳인지 숫자인지 -> 근데 이거 테스트할 떄마다 새롭게 정의해야댐
let pattern = /[a-z]/g;
console.log(pattern.test("a"));
let pattern2 = /[0-9]/g;
console.log(pattern.test("1"))


// 정규 표현식 변수 일반화 -> 하나만 바꿀 때 사용할 수 있음
let str = "abcdasdf";
let target = "a"

let pattern = new RegExp(`${target}`, "g");
str = str.replace(pattern, "1");
console.log(str);



******* 정리 *******
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







22. 문자열, 배열 비어있는지 체크 -> length로 통일하자.


let str = "";

if (str) { // 가능
  console.log(1);
}
if (str.length) { // 가능
  console.log(111);
}

let arr = [];

if (arr) { // 불가능
  console.log(111);
}
if (arr.length) { // 가능
  console.log(222);
}


23. 진법 변환

/**
 * 진수 변환
 *
 * 10진수를 진수 변환할때는 Number객체의 내장 함수인 toString()을 사용한다.
 * 10진수 외의 다른 진수를 10진수로 변환할때는 전역 함수인 parseInt()을 사용한다.
 */

// 1. 10진수 -> 2진수
let 십진수 = 125;
console.log(`1. 10진수(${십진수}) -> 2진수(${십진수.toString(2)})`); // 1111101

// 2. 10진수 -> 8진수
console.log(`2. 10진수(${십진수}) -> 8진수(${십진수.toString(8)})`); // 175

// 3. 10진수 -> 16진수
console.log(`3. 10진수(${십진수}) -> 16진수(${십진수.toString(16)})`); // 7d

// 4. 2진수 -> 8진수
let 이진수 = "1111101";
console.log(`4. 2진수(${이진수}) -> 8진수(${parseInt(이진수, 2).toString(8)})`); // 175

// 5. 2진수 -> 10진수
console.log(`5. 2진수(${이진수}) -> 10진수(${parseInt(이진수, 2)})`); // 125

// 6. 2진수 -> 10진수
console.log(`6. 2진수(${이진수}) -> 16진수(${parseInt(이진수, 2).toString(16)})`); // 7d

// 7. 8진수 -> 2진수
let 팔진수 = "175";
console.log(`7. 8진수(${팔진수}) -> 2진수(${parseInt(팔진수, 8).toString(2)})`); // 1111101

// 8. 8진수 -> 10진수
console.log(`8. 8진수(${팔진수}) -> 10진수(${parseInt(팔진수, 8)})`); // 125

// 9. 8진수 -> 16진수
console.log(`9. 8진수(${팔진수}) -> 16진수(${parseInt(팔진수, 8).toString(16)})`); // 7d




24. swap

let arr = [1, 2, 3, 4];

[arr[0], arr[1]] = [arr[1], arr[0]];

console.log(arr);


```
