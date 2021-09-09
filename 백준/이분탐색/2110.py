# 실버1 - 공유기 설치
# 이분탐색


# 전형적인 마굿간 형태 문제
# 그리디, 디피, 완탐 모두 적용 불가능
# 파라메트릭 서치로 변경해서 푼다.

# 이런 유형은 외워야함


n, c = map(int, input().split())
homes = [int(input()) for _ in range(n)]
homes.sort()

lt = 1
rt = max(homes)
res = 0


def count(capa):
    cnt = 1
    prev = homes[0]
    for i in range(1, n):
        if homes[i] - prev >= capa:
            cnt += 1
            prev = homes[i]
    if cnt >= c:
        return True
    else:
        return False


while lt <= rt:
    mid = (lt+rt) // 2
    if count(mid):
        lt = mid + 1
        res = mid
    else:
        rt = mid - 1

print(res)
