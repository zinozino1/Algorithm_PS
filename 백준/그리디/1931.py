# 실버2 - 회의실 배정
# 그리디


# 1. 완전탐색 DFS(부분집합)? -> n=10만
# 2. dp vs 그리디
# 우선 그리디 먼저 시도해본다. (정렬 + 시작시간 & 끝시간 기준 판단 )

n = int(input())
target = [tuple(map(int, input().split())) for _ in range(n)]

target.sort(key=lambda x: (x[1], x[0]))
cnt = 1
end = target[0][1]
for i in range(1, len(target)):
    start = target[i][0]

    if start >= end:
        end = target[i][1]
        cnt += 1

print(cnt)
