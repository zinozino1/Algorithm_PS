
import sys
input = sys.stdin.readline


def sol():
    index = 1
    while True:
        res = tuple(map(int, input().split()))
        if res == (0, 0, 0):

            break
        # res[0] == L
        # res[1] == P
        # res[2] == V

        cnt = 0
        if res[2] % res[1] < res[0]:
            cnt += (res[2]//res[1]) * res[0] + res[2] % res[1]
        else:
            cnt += (res[2]//res[1]) * res[0] + res[0]
        print("Case %d: %d" % (index, cnt))
        index += 1

sol()
