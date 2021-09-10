# 트리
# 2시간


import sys
sys.setrecursionlimit(10**6)


def postorderTraverse(v, arr, tree):
    if v == -1:
        return
    postorderTraverse(tree[v][0], arr, tree)
    postorderTraverse(tree[v][1], arr, tree)
    arr.append(v)


def preorderTraverse(v, arr, tree):
    if v == -1:
        return
    arr.append(v)
    preorderTraverse(tree[v][0], arr, tree)
    preorderTraverse(tree[v][1], arr, tree)


def makeTree(v, nodeinfos, idx, tree, check, left_parent, right_parent):

    x, y, parent = nodeinfos[v]
    left_idx, left_val = -1, -1
    right_idx, right_val = -1, -1

    for i in range(idx+1, len(nodeinfos)):
        if nodeinfos[i][0] < x and nodeinfos[i][1] < y and check[i] == 0:
            if not left_parent:
                left_idx, left_val = i, nodeinfos[i][2]
                break
            elif nodeinfos[i][0] > left_parent[len(left_parent)-1]:
                left_idx, left_val = i, nodeinfos[i][2]
                break
    for i in range(idx+1, len(nodeinfos)):
        if nodeinfos[i][0] > x and nodeinfos[i][1] < y and check[i] == 0:
            if not right_parent:
                right_idx, right_val = i, nodeinfos[i][2]
                break
            elif nodeinfos[i][0] < right_parent[len(right_parent)-1]:
                right_idx, right_val = i, nodeinfos[i][2]
                break

    if left_idx != -1:
        check[left_idx] = 1
        tree[parent].append(left_val)
        right_parent.append(x)
        makeTree(left_idx, nodeinfos, left_idx, tree,
                 check, left_parent, right_parent)
        right_parent.pop()
    else:
        tree[parent].append(-1)

    if right_idx != -1:
        check[right_idx] = 1
        tree[parent].append(right_val)
        left_parent.append(x)
        makeTree(right_idx, nodeinfos, right_idx, tree,
                 check, left_parent, right_parent)
        left_parent.pop()
    else:
        tree[parent].append(-1)


def solution(nodeinfo):
    nodeinfos = [[v[0], v[1], i+1] for i, v in enumerate(nodeinfo)]
    nodeinfos.sort(key=lambda x: (-x[1], x[0]))

    check = [0]*len(nodeinfos)
    tree = {}
    for i in range(1, len(nodeinfos)+1):
        tree[i] = []
    makeTree(0, nodeinfos, 0, tree, check, [], [])

    root = nodeinfos[0][2]
    pre_order = []
    preorderTraverse(root, pre_order, tree)
    post_order = []
    postorderTraverse(root, post_order, tree)

    return [pre_order, post_order]
