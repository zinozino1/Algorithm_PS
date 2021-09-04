# 골드5 - 트리
# 트리



from collections import defaultdict

n = int(input())
parents = list(map(int, input().split()))
target = int(input())
tree = defaultdict(list)
for i in range(n):
    tree[i] = [parents[i], []]
for i in range(n):
    if parents[i] != -1:
        tree[parents[i]][1].append(i)


def removeNode(node):
    tmp = tree[node][1][:]
    tree[node] = []
    for nxt in tmp:
        removeNode(nxt)


# 부모에서 타겟 삭제
if tree[target][0] != -1:
    tree[tree[target][0]][1].remove(target)

# 타겟부터 자식 모두 삭제
removeNode(target)

cnt = 0
for node in tree.keys():
    if tree[node] and not tree[node][1]:
        cnt += 1

print(cnt)
