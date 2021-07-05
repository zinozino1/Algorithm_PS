# two pointer
class Solution:
    def reverseString(self, s: List[str]) -> None:
        lt, rt = 0, len(s)-1
        while lt <= rt:
            s[lt], s[rt] = s[rt], s[lt]
            lt += 1
            rt -= 1
