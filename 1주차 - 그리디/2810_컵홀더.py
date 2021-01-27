# 3가지 경우의수로 풀었음
# 그리디를 적용하지 않고 단순 구현한듯


import sys
input = sys.stdin.readline


def sol():
    n = int(input())
    seats = input()

    cnt = 0

    if 'L' in seats and 'S' in seats:
        cnt = seats.count("L") // 2 + seats.count("S") + 1
    elif "L" in seats and 'S' not in seats:
        cnt = seats.count("L") // 2 + 1
    elif "L" not in seats and "S" in seats:
        cnt = seats.count("S")

    print(cnt)


sol()
