# 골드4 - 순회 강연
# 그리디

# 반례때문에 한참 고민했음
# 힙을 사용하는 방법도 있으나 내 풀이가 가장 직관적이라 생각

n = int(input())
target = [tuple(map(int, input().split())) for _ in range(n)]
target.sort(key=lambda x: (x[1], -x[0]))
check = [0]*10001
res = 0
for i in range(n):
    p, d = target[i]
    # 비어있는 곳에 강연료 할당
    for j in range(1, d+1):
        if check[j] == 0:
            check[j] = p
            break
    else:  # 꽉 찼을 경우 가장 작은 강연료를 바꿔야함
        tmp_min = 1e9
        idx = -1
        for j in range(1, d+1):
            if tmp_min > check[j]:
                idx = j
                tmp_min = check[j]
        if idx != -1 and tmp_min < p:
            check[idx] = p
print(sum(check))
