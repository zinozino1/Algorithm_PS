# 골드5-탑
# 스택 활용₩1

# 스택에 내림차순으로 쌓으면 O(N)이다

n = int(input())
towers = list(map(int, input().split()))
stack = [(towers[0], 0)]

max_idx = 0
max_val = towers[0]
res = [0]*n

for i in range(1, n):

    while stack and stack[-1][0] < towers[i]:
        stack.pop()
    if stack and stack[-1][0] > towers[i]:
        res[i] = stack[-1][1]+1

    stack.append((towers[i], i))
    if max_val > towers[i]:
        max_val = towers[i]
        max_idx = i

print(*res)
