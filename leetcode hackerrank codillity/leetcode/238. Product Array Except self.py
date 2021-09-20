# 단순 반복

# 내 풀이 -> o(n)으로 풀긴함 근데 나누기 연산자 씀
class Solution:
    def productExceptSelf(self, nums: List[int]):
        mult = 1
        res = []
        except_zero_mult = 1
        mult = 1
        if nums.count(0) > 1:
            return [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                except_zero_mult *= nums[i]
            mult *= nums[i]
        for i in range(len(nums)):
            if nums[i] == 0:
                res.append(except_zero_mult)
            else:
                res.append(mult//nums[i])
        return res

# 다시 푼 것 -> 나누기 안쓰고 o(n) -> 정방향 누적곱과 역방향 누적곱 이용


class Solution:
    def productExceptSelf(self, nums: List[int]):
        mult = [0]*len(nums)
        mult[0] = nums[0]
        reverse_mult = [0]*len(nums)
        reverse_mult[len(nums)-1] = nums[len(nums)-1]

        for i in range(1, len(nums)):
            mult[i] = nums[i]*mult[i-1]
        for i in range(len(nums)-2, -1, -1):
            reverse_mult[i] = nums[i]*reverse_mult[i+1]

        res = [0]*len(nums)
        res[0] = reverse_mult[1]
        res[len(nums)-1] = mult[len(nums)-2]
        for i in range(len(nums)-2):
            res[i+1] = mult[i]*reverse_mult[i+2]
        return res
