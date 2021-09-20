# 스택


# 스택에 값이 아닌 인덱스를 집어넣는다.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                pop = stack.pop()
                res[pop] = i-pop
            stack.append(i)

        return res
