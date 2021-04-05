# 골드4-그리디-수묶기
# 너무 더럽게 품..
# 원소들을 정렬하여 그리디방식으로 풀 수 있음
# 예외케이스들을 하나하나 생각해봐야한다.

import sys
input = sys.stdin.readline


def sol():

    n = int(input())
    target = [int(input()) for _ in range(n)]

    target.sort(reverse=True)

    ptr = 1
    res = 0
    while True:

        if ptr > n-1:
            break
        # 원소가 0보다 작거나 같은가
        if target[ptr] <= 0:
            # 바로 앞 원소가 0보다 큰가 => 양수인 원소가 홀수
            if target[ptr-1] > 0:
                res += target[ptr-1]
                ptr += 1
                if ptr == n:
                    # 마지막 양수 원소 더해줌
                    res += target[-1]
                continue

                # 음수부터는 따로 배열 만들어 다시 정렬
            tmp = []
            if target[ptr-1] <= 0:
                tmp = target[ptr-1:n]
            else:
                tmp = target[ptr:n]
            tmp.sort()

            # 음수 처리
            ptr2 = 1
            while True:

                if tmp[ptr2] == 0:
                    ptr2 += 1
                    if ptr2 == len(tmp):
                        ptr = n
                        break
                else:
                    res += tmp[ptr2] * tmp[ptr2-1]
                    ptr2 += 2
                    # 음수가 홀수개
                    if ptr2 == len(tmp):
                        res += tmp[-1]
                        ptr = n
                        break
                    # 음수가 짝수개
                    elif ptr2 > len(tmp):
                        ptr = n
                        break

        # 원소가 양수인가
        else:
            if target[ptr] == 1:
                res += target[ptr-1]
                ptr += 1
                if ptr == n:
                    res += target[-1]
            else:
                res += target[ptr] * target[ptr-1]
                ptr += 2
                # 홀수개면 마지막 원소 더해줌
                if ptr == n:
                    res += target[-1]

    if len(target) == 1:
        print(target[0])
    else:
        print(res)


sol()
