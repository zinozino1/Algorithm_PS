# 해시
import heapq
from collections import Counter
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1

        tmp = []
        for key in dic.keys():
            tmp.append((key, dic[key]))

        tmp.sort(key=lambda x: (-x[1]))
        res = []
        for i in range(k):
            res.append(tmp[i][0])

        return res


# 해시(카운터) + 힙


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter = Counter(nums).most_common(k) -> 지리는 방법 1
        counter = Counter(nums)
        heap = []
        for key in counter.keys():
            heapq.heappush(heap, (-counter[key], key))
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
