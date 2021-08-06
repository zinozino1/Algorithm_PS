# 실버3 - 수들의 합 2
# 투포인터

# 기본 투포인터 lt=0 rt=0으로 시작하자

n, m = map(int, input().split())
arr = list(map(int, input().split()))

lt = 0
rt = 0
tot = 0
cnt = 0
while True:
    if tot < m:
        if rt == n:
            break
        tot += arr[rt]
        rt += 1
    elif tot > m:
        if lt == n:
            break
        tot -= arr[lt]
        lt += 1
    else:
        cnt += 1
        tot -= arr[lt]
        lt += 1

print(cnt)
