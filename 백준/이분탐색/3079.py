# 실버1 - 입국 심사
# 이분 탐색 


n, m = map(int, input().split())
candi = [int(input()) for _ in range(n)]

lt = 1
rt = max(candi) * m


def cal(capa):
    res = 0
    for can in candi:
        res += capa // can
    return res


ans = 0
while lt <= rt:
    mid = (lt+rt) // 2

    if cal(mid) >= m:
        rt = mid - 1
        ans = mid
    else:
        lt = mid + 1

print(ans)
