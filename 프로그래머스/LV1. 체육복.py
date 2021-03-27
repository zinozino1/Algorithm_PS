# 그리디
# 일단 정렬후 lt,rt이용해서 순차적으로 가면 된다
# lt,rt 자체가 단계의 최적 선택

def solution(n, lost, reserve):

    lt = 0
    rt = 0
    cnt = 0
    lost.sort()
    reserve.sort()
    while True:
        # rt -> reserve lt -> lost
        if rt == len(reserve) or lt == len(lost):
            break
        # 체육복을 빌려줄 수 있으면
        if reserve[rt] - 1 == lost[lt] or reserve[rt] + 1 == lost[lt]:
            # 근데 여분의 체육복 있는넘이 잃어버린 경우
            if reserve[rt] in lost:
                lt += 1
            elif lost[lt] in reserve:
                rt += 1
            # 체육복 빌려주기
            else:
                cnt += 1
                lt += 1
                rt += 1
        # 체육복을 빌려줄 수 없음
        else:
            if lost[lt] > reserve[rt]:
                rt += 1
            elif lost[lt] < reserve[rt]:
                lt += 1
            elif lost[lt] == reserve[rt]:
                cnt += 1
                lt += 1
                rt += 1

    return n-len(lost)+cnt
