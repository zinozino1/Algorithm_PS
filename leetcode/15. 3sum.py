# 투포인터


# 내 풀이 -> 분명 o(n^2)로 짜냈는데 왜 TLE지
from collections import defaultdict


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        two_sum = defaultdict(list)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                two_sum[nums[i]+nums[j]].append((i, j))
        res = set()
        for i in range(len(nums)):
            if two_sum[-nums[i]]:
                for item in two_sum[-nums[i]]:
                    if i not in item:
                        res.add(
                            tuple(sorted([nums[i], nums[item[0]], nums[item[1]]])))
        return list(res)


# 최적화 풀이 -> 배열 순회하며 오른쪽 기준 투포인터 돌리기

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums) - 2):
            lt, rt = i+1, len(nums)-1
            while lt < rt:
                tot = nums[i]+nums[lt]+nums[rt]
                if tot == 0:
                    res.add(tuple([nums[i], nums[lt], nums[rt]]))
                    lt += 1
                    rt -= 1
                elif tot > 0:
                    rt -= 1
                elif tot < 0:
                    lt += 1

        return list(res)
