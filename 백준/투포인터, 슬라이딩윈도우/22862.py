# 실버1 - 가장 긴 짝수 부분수열
# 투포인터

# 우선 이건 dp로 못푼다
# 최대 k개를 제외해야한다는 조건이 있기 때문
# 슬라이딩 윈도우 형태로 k 리미트에 맞춰 포인터들을 이동시킴


n, k = map(int, input().split())
seq = list(map(int, input().split()))

lt, rt = 0, 0
res = 0

ans = -1e9
while lt < n and rt < n:
    if seq[rt] % 2 == 1:  # 홀수
        if k == 0:
            if seq[lt] % 2 == 0:
                res -= 1
            else:
                k += 1
            lt += 1
        else:
            k -= 1
            rt += 1

    else:  # 짝수
        rt += 1
        res += 1

    ans = max(ans, res)

print(ans)
