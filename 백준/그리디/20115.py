# 실버3 - 에너지 드링크
# 그리디

# 가장 작은 음료를 계속 나눠줘야함

import math
n = int(input())
target = list(map(int, input().split()))
target.sort(reverse=True)
res = target[0]
for i in range(1, n):
    res += target[i] / 2
if math.ceil(res) == math.floor(res):
    print(int(res))
else:
    print(res)
