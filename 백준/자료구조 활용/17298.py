# 골드4-오큰수
# 스택활용하여 품
# 값 넣기 전에 넣으려는 수보다 작은 것들 모두 뺌

n = int(input())
target = list(map(int, input().split()))
stack = []
res = [0]*n

for i, v in enumerate(target):
    if stack and v > stack[-1][0]:
        while stack and stack[-1][0] < v:
            curr = stack.pop()
            res[curr[1]] = v
        stack.append((v, i))
    else:
        stack.append((v, i))

for i in range(n):
    if res[i] == 0:
        res[i] = -1

print(*res)
