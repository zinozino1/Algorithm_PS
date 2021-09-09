# 실버4 - 로프
# 그리디

# 로프 순서 상관 없으므로 정렬 후 남은 갯수만큼 곱해서 계산


n = int(input())
weight = [int(input()) for _ in range(n)]
weight.sort()

max_weight = -1e9
for i in range(n):
    max_weight = max(max_weight, weight[i] * (n-i))

print(max_weight)
