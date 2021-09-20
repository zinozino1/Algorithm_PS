# 문자열 + 해시
# 풀이시간 : 약 7분

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            dic["".join(sorted(s))] = []
        for s in strs:
            dic["".join(sorted(s))].append(s)
        res = []
        for key in dic.keys():
            res.append(dic[key])
        return res


# 개선된 풀이 -> defaultdict 이용


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            dic["".join(sorted(s))].append(s)
        return list(dic.values())
