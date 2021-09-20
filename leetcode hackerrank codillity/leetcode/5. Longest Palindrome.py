# 문자열 + 투포인터 + 슬라이딩 윈도우
# 정석적인 브루트포스를 이용했으나 TLE


# 내 풀이 (TLE)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = -1e9
        res = ''
        check = {}
        for i in range(len(s)):
            for j in range(i, len(s)):
                if check.get(s[i:j+1]):
                    continue
                if s[i:j+1] == "".join(list(s[i:j+1])[::-1]):
                    check[s[i:j+1]] = len(s[i:j+1])
                    if len(s[i:j+1]) > max_len:
                        max_len = len(s[i:j+1])
                        res = s[i:j+1]
        return res


# 답 - 투포인터 + 슬라이딩 윈도우
class Solution:
    def longestPalindrome(self, s: str) -> str:

        # 해당 문자열이 팰린드롬이면 중앙 기준으로 확장
        def is_palindrome(left, right):
            while 0 <= left and right <= len(s) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left+1:right-1]

        # 예외처리
        if len(s) < 2 or s == s[::-1]:
            return s
        res = ''

        # 슬라이딩 윈도우 -> 홀수, 짝수 윈도우를 문자열 끝까지 슬라이딩 시킴
        for i in range(len(s)-1):
            res = max(res, is_palindrome(i, i+1),
                      is_palindrome(i, i+2), key=len)
        return res
