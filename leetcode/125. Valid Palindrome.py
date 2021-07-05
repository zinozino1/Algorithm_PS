# 문자열
# 풀이시간 : 3분
import re


class Solution:  # 내 풀이
    def isPalindrome(self, s: str) -> bool:
        tmp = ''
        for c in s:
            if c.isalnum():
                tmp += c
        tmp = tmp.lower()
        print(tmp)
        return True if tmp == tmp[::-1] else False


class Solution:  # 정규 표현식 풀이
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', "", s)
        return s == s[::-1]
