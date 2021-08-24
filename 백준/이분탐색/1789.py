# 실버5 - 수들의 합
# 이분탐색

# n을 이분탐색. 1~n까지의 합이 s 이하면 lt = mid +1 s 초과면 rt = mid - 1

# 만약 19 면 (19*20)//2 = 190
# 20이면 = 210

s = int(input())
lt, rt = 1, s
ans = 0
while lt <= rt:
    m = (lt + rt) // 2
    if m * (m+1) // 2 > s:
        rt = m - 1
    else:
        ans = m
        lt = m + 1
print(ans)
