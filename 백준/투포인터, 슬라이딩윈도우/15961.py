# 골드4 - 회전 초밥
# 슬라이딩 윈도우

# 중복되지 않는 원소의 개수를 최대로 하는 k개의 연속된 구간을 찾아내는 문제
# 카운터 체크 배열이 중요

from collections import deque

n, d, k, c = map(int, input().split())
cho = [int(input()) for _ in range(n)]
counter = [0]*(d+1)
window = deque()
for i in range(k):
    counter[cho[i]] += 1
    window.append(cho[i])

final = len(counter)-counter.count(0)
res = len(counter)-counter.count(0)

lt = 1
rt = k

while lt <= n:
    curr = window.popleft()
    if counter[curr] > 1:
        counter[curr] -= 1
    elif counter[curr] == 1:
        res -= 1
        counter[curr] -= 1

    window.append(cho[rt])
    if counter[cho[rt]] == 0:
        counter[cho[rt]] += 1
        res += 1
    else:
        counter[cho[rt]] += 1

    if counter[c] == 0:
        final = max(final, res+1)
    else:
        final = max(final, res)
    lt += 1
    rt = (rt+1) % n

print(final)
