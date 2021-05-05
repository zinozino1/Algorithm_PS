# 첫번째 트라이 - 단순 반복문
# 정확성 통과 효율성 실패

def solution(stones, k):

    cnt = 0
    flag = False
    while True:
        innerCnt = 0
        for i in range(len(stones)):
            if stones[i] == 0:
                innerCnt += 1
                if innerCnt == k:
                    flag = True
                    break
            else:
                innerCnt = 0

        if flag:
            break
        for i in range(len(stones)):
            if stones[i] > 0:
                stones[i] -= 1
        cnt += 1

    return cnt

# 두번째 트라이 - 이분탐색
# 정확성, 효율성 통과


def solution2(stones, k):

    lt = 1
    rt = 200000000
    res = 0
    while lt <= rt:
        # 인원수
        mid = (lt+rt)//2
        tmp = stones[:]
        # 돌 숫자에서 인원수 빼면
        for i in range(len(tmp)):
            tmp[i] -= mid
        cnt = 0
        flag = False
        # 연속된 0이하의 징검다리 개수 세기
        for i in range(len(tmp)):
            if tmp[i] <= 0:
                cnt += 1
                if cnt == k:
                    flag = True
            else:
                cnt = 0

        # 연속된 0이하의 징검다리 개수가 k와 같거나 크다면 인원수 줄이기
        if flag:
            rt = mid - 1
            res = mid
        # 아니면 인원수 늘리기
        else:
            lt = mid + 1

    return res
