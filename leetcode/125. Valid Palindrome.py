# 문자열
# 풀이시간 : 3분
class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ''
        for c in s:
            if c.isalnum():
                tmp += c
        tmp = tmp.lower()
        print(tmp)
        return True if tmp == tmp[::-1] else False
