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

# 고수풀이

# n 입력받기
n = int(input())

# 양수 리스트 초기화하기
pn = []
# 음수 리스트 초기화하기
nn = []
# 나머지 수 리스트 초기화하기
en = []
# 리스트에 숫자 집어넣기
for i in range(n):
    number = int(input())
    # number가 1보다 크면 양수리스트에 추가하기
    if number > 1:
        pn.append(number)
    # 0보다 작으면 음수리스트에 추가하기
    elif number < 0:
        nn.append(number)
    else:
        en.append(number)

# 양수리스트 큰순으로 정렬하기
pn.sort(reverse=True)
# 음수리스트 작은순으로 정렬하기
nn.sort()

# 정답 변수 초기화하기
result = 0
# pn 길이가 짝수이면 그냥하고 홀수이면 남은 한개는 더해주기
if len(pn) % 2 == 0:
    for i in range(0, len(pn)-1, 2):
        result += pn[i]*pn[i+1]
if len(pn) % 2 != 0:
    for i in range(0, len(pn)-1, 2):
        result += pn[i]*pn[i+1]
    result += pn[-1]

# nn 길이가 짝수이면 그냥하고 홀수이면 남은 한개는 더해주기
if len(nn) % 2 == 0:
    for i in range(0, len(nn)-1, 2):
        result += nn[i]*nn[i+1]
if len(nn) % 2 != 0:
    for i in range(0, len(nn)-1, 2):
        result += nn[i]*nn[i+1]
    # 나머지 수에 0이 없다면 그냥 더해주기
    if 0 not in en:
        result += nn[-1]
# en에 있는 1들 다 더해주기
result += sum(en)
print(result)
