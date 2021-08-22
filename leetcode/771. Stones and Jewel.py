# hash

from collections import defaultdict


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = defaultdict(int)
        for j in jewels:
            dic[j] += 1
        cnt = 0
        for s in stones:
            if dic.get(s):
                cnt += 1
        return cnt
