# 투포인터

# 내 풀이 -> o(nlogn)으로 풀었으나 속도 아직 느림
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = [tuple((i, v)) for i, v in enumerate(nums)]
        tmp.sort(key=lambda x: (x[1]))
        lt, rt = 0, len(tmp)-1
        while lt <= rt:
            if tmp[lt][1] + tmp[rt][1] == target:
                return [tmp[lt][0], tmp[rt][0]]
            else:
                if tmp[lt][1] + tmp[rt][1] > target:
                    rt -= 1
                else:
                    lt += 1


# 최적화 풀이 -> 타겟에서 첫번째 값을 뺀 값을 딕셔너리에서 찾기 o(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, v in enumerate(nums):
            dic[v] = i
        for i, v in enumerate(nums):
            if target-v in dic and i != dic[target-v]:
                return [i, dic.get(target-v)]
