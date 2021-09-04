# 실버1 - 완전 이진 트리
# 트리


# 내 풀이 -> 트리 생성 하지 않고 배열로만 풀음
k = int(input())
order = list(map(int, input().split()))

for i in range(k, 0, -1):
    for j in range(2**(i-1)-1, len(order), 2**i):
        print(order[j], end=" ")
    print()


# 트리 생성하는 풀이 -> 이진트리 중위순회를 바탕으로 트리 생성하는 법


# 완전 이진 트리의 높이
k = int(input())
# 완전 이진 트리 중위순회결과
inorder = list(map(int, input().split()))
# 전체 완전 이진 트리 구조
tree = [[] for _ in range(k)]


def makeTree(order, depth):
    mid = len(order) // 2
    tree[depth].append(order[mid])
    if len(order) == 1:
        return
    makeTree(order[:mid], depth+1)
    makeTree(order[mid+1:], depth+1)


makeTree(inorder, 0)
print(tree)
