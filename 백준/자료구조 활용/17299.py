# 골드5-오등큰수
# 17298과 유사
# 중복된 갯수를 Counter 모듈로 구현

from collections import Counter

n = int(input())
target = list(map(int, input().split()))
stack = []
dic = Counter(target)
res = [0] * n

for i, t in enumerate(target):
    if stack and stack[-1][0] < dic[t]:
        while stack and stack[-1][0] < dic[t]:
            curr = stack.pop()
            res[curr[1]] = t
        stack.append((dic[t], i))
    else:
        stack.append((dic[t], i))

for i in range(n):
    if res[i] == 0:
        res[i] = -1

print(*res)
