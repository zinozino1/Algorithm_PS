# 실버4 - 보물
# 정렬, 그리디

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = 0
for i in range(n):
    minN = min(a)
    maxN = max(b)
    res += minN*maxN
    a.remove(minN)
    b.remove(maxN)

print(res)
