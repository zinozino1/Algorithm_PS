# 실버1 - 이진 탐색 트리
# 트리


# 전위 순회 결과를 보고 자신보다 더 커지거나 작아지는 순간이 자식 노드이다.

from collections import defaultdict
import sys
sys.setrecursionlimit(10000)


order = []
while True:
    try:
        order.append(int(input()))
    except:
        break

check = [0]*len(order)
check[0] = 1
tree = defaultdict(list)


def traverse(node):
    if node == -1:
        return
    else:
        traverse(tree[node][0])
        traverse(tree[node][1])
        print(node)


def makeTree(nodeIdx, depth):
    minIdx = -1
    maxIdx = -1
    for i in range(nodeIdx+1, len(order)):
        if check[i] == 1:
            break
        if order[i] < order[nodeIdx] and check[i] == 0:
            minIdx = i
            break
    for i in range(nodeIdx+1, len(order)):
        if check[i] == 1:
            break
        if order[i] > order[nodeIdx] and check[i] == 0:
            maxIdx = i
            break
    if minIdx != -1:
        check[minIdx] = 1
    if maxIdx != -1:
        check[maxIdx] = 1

    if minIdx != -1:
        tree[order[nodeIdx]].append(order[minIdx])
        makeTree(minIdx, depth+1)
    else:
        tree[order[nodeIdx]].append(-1)
    if maxIdx != -1:
        tree[order[nodeIdx]].append(order[maxIdx])
        makeTree(maxIdx, depth+1)
    else:
        tree[order[nodeIdx]].append(-1)


makeTree(0, 0)

traverse(order[0])
