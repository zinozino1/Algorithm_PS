# 투포인터 + 해시

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = defaultdict(int)
        lt = 0
        rt = 0
        maxLen = -1e9

        while rt < len(s):
            if(not dic.get(s[rt]) or dic.get(s[rt]) == 0):
                dic[s[rt]] += 1
                rt += 1
            else:
                dic[s[lt]] -= 1
                lt += 1
            maxLen = max(maxLen, rt-lt)

        if maxLen == -1e9:
            return len(s)
        else:
            return maxLen
