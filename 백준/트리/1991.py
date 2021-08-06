# 실버1 - 트리순회
# 트리

# 트리 순회는 그래프 순회와 결이 다르다


from collections import defaultdict
n = int(input())
tree = defaultdict(list)
for _ in range(n):
    r, lt, rt = input().split()
    tree[r].append(lt)
    tree[r].append(rt)


def preorder(v):
    print(v, end="")
    if tree[v][0] != ".":
        preorder(tree[v][0])
    if tree[v][1] != ".":
        preorder(tree[v][1])


def inorder(v):
    if tree[v][0] != ".":
        inorder(tree[v][0])
    print(v, end="")
    if tree[v][1] != ".":
        inorder(tree[v][1])


def postorder(v):
    if tree[v][0] != ".":
        postorder(tree[v][0])
    if tree[v][1] != ".":
        postorder(tree[v][1])
    print(v, end="")


preorder("A")
print()
inorder("A")
print()
postorder("A")
print()
