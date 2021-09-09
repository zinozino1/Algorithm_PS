# 실버3 - 예산
# 이분탐색

# 접근 :
# 1. tmp를 1부터 total 까지 설정한 다음에 tmp에 대해 budget 루프롤 돌린다
# -> 10만 * 1만이므로 TLE
# 2. 이분탐색 -> 10만짜리 탐색을 이분탐색으로 log10만 으로 만든다.


# 전형적 이분탐색 문제.
# rt를 잡을 때 10만이나, total로 잡으면 안된다. 모든 지방의 예산 금액 합이 M을 초과하지 않는다면 답은 지방의 요구 금액 최댓값이기 때문



n = int(input())
budget = list(map(int, input().split()))
total = int(input())

lt = 1
rt = max(budget)


def judge(capa):
    tmp = 0
    for b in budget:
        if b > capa:
            tmp += capa
        else:
            tmp += b
    return True if tmp <= total else False


res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if judge(mid):
        lt = mid + 1
        res = mid
    else:
        rt = mid - 1

print(res)
