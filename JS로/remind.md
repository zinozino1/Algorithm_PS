```js



1. 정렬

-> 기본 정렬 되지 않으므로 람다함수 넣어줘야함
-> [3,2,1]
-> arr.sort((a,b) => a-b)
// 2차원 배열은 이렇게
->[[1,2],[2,3],[2,1]]
-> arr.sort((a,b) => a[0] === b[0] ? b[1]-a[1]:a[0]-b[0])
-> 0번 인덱스 기준 정렬  + 0번이 같다면 1번 다시 기준

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






6. 문자열 특정 값 변경 -> String.prototype 메서드는 기본적으로 원본 변경 x

let str = "ABCDEFFFFF"
-> let tmp = str.replace(/F/g, "#")

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





11. 배열 원소들 출력

-> let arr = [1,2,3]
# 123
let a1 = arr.join("")
# 1,2,3
let a2 = arr.join(",")





11. 배열 첫번쨰자리, 마지막자리 원소 삽입

let arr = [1,2,3]
arr.push(4) // 마지막 자리
arr.unshift(0) // 첫번쨰 자리





12. 딕셔너리 쓰기

let obj = {} 으로 가능




13. 문자열 배열 sorting
-> 알파벳순으로 소팅됨




14. 문자열 -> 배열
let str = "abc"
let arr = Array.from(str)




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
console.log(arr.reduce((a, v, i) => a + v));






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

let char2 = "b";
let str2 = "aaaaaaaaa";

while (str2.indexOf("a") !== -1) { // 포함되어 있지 않다를 표현
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





22. 문자열, 배열 비어있는지 체크


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


```
