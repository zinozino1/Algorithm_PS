# 쉬운 정렬문제

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(0, len(nums)-1, 2):
            res += min(nums[i], nums[i+1])
        return res
