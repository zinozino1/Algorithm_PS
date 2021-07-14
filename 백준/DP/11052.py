# 실버1-카드 구매하기
# dp
# 직관적인 풀이가 떠오르지 않아 테스트케이스 일일히 나열하여 풀었으나 반례존재
# 힌트 보고 다시 풀었음


# -> 잘못된 풀이였음 dp끼리 더하는 것이 아닌 dp와 value를 더한 값을 최대로 하는 거였음

# 약 30분

n = int(input())
packs = list(map(int, input().split()))
packs.insert(0, 0)

if n == 1:
    print(packs[1])
elif n == 2:
    print(max(packs[2], packs[1]*2))
else:
    dp = [0]*(n+1)
    dp[1] = packs[1]
    dp[2] = max(dp[1]*2, packs[2])
    dp[3] = max(dp[1]*3, dp[2]+dp[1], packs[3])

    for i in range(4, n+1):
        tmp_max = -1e9
        for j in range(i, i//2, -1):
            if dp[j]+dp[i-j] > tmp_max:
                tmp_max = dp[j]+dp[i-j]
        if i % 2 == 0:
            dp[i] = max(packs[i], tmp_max, packs[i//2]*2)
        else:
            dp[i] = max(packs[i], tmp_max)
    # print(dp)
    print(dp[-1])


# 개선된 풀이
# -> 카드 i 개를 구매하는 최대 비용 packs[k] + dp[i-k]
N = int(input())
card = [0]
card += list(map(int, input().split()))

dp = [0] * (N+1)
dp[1] = card[1]
dp[2] = max(card[2], card[1]*2)

for i in range(3, N+1):
    dp[i] = card[i]  # 자기 자신으로 만드는 경우
    for j in range(1, i//2 + 1):  # j와 i-j로 만드는 경우
        dp[i] = max(dp[i], dp[j] + dp[i-j])

print(dp[N])
