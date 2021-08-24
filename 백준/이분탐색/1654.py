# 실버3 - 랜선 자르기
# 이분탐색

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]


lt = 1
rt = max(lan)
res = 0

while lt <= rt:
    mid = (lt+rt) // 2
    if sum(l//mid for l in lan) >= n:
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)
