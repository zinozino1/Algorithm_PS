# 투 포인터

# 내 풀이 -> 확장 슬라이딩 윈도우 ->  반례때매 실패
class Solution:
    def trap(self, height: List[int]) -> int:

        def expand(lt, rt):
            while 0 <= lt and rt <= len(height)-1 and height[lt-1] > height[lt] and height[rt+1] > height[rt]:
                lt -= 1
                rt += 1
            inner_sum = 0
            for i in range(1, len(height[lt:rt+1])-1):
                inner_sum += height[lt:rt+1][i]
            return (rt-lt-1)*min(height[lt], height[rt]) - inner_sum

        res = 0
        for i in range(len(height)-2):
            if height[i:i+3][0] > height[i:i+3][1] and height[i:i+3][1] < height[i:i+3][2]:
                res += expand(i, i+2)
        return res


# 답 -> 투포인터
# 좌우 어느쪽이든 낮은쪽이 높은쪽을 향해서 포인터가 가운데로 점점 이동한다
# o(n)으로 해결 가능

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        lt, rt = 0, len(height)-1
        l_max, r_max = height[lt], height[rt]
        res = 0
        while lt < rt:
            l_max, r_max = max(height[lt], l_max), max(height[rt], r_max)
            if l_max <= r_max:
                res += l_max - height[lt]
                lt += 1
            else:
                res += r_max - height[rt]
                rt -= 1
        return res
