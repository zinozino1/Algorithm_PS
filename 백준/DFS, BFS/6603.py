# 실버2-로또
# DFS 조합


import itertools as it
while True:
    target = list(map(int, input().split()))
    if target[0] == 0:
        break

    n, nums = target[0], target[1:]

    for tmp in it.combinations(nums, 6):
        print(*list(tmp))
    print()
