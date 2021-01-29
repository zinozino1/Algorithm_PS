
import sys
input = sys.stdin.readline


def sol():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a.sort(reverse=True)

    maxN = -1e9

    for i in range(n):
        if a[i] * (i+1) > maxN:
            maxN = a[i] * (i+1)

    print(maxN)

sol()
