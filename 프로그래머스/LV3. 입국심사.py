# 이분탐색
# 입력값이 굉장히 크므로 이분탐색을 먼저 고민
# 이분탐색 범위의 최소값과 최대값을 구하는 것이 중요
# 최대값은 가장 빠르게 심사하는 사람 * 사람 수
# 최소값은 가장 빠르게 심사하는 사람의 걸리는 시간
# 근데 최대 10억 최소 1로 잡아도 정답 나옴
# Worst case를 계속적으로 탐색하는 듯함

def solution(n, times):
    times.sort()

    largest = times[0] * n  # 100000000000
    smallest = times[0]  # 1

    def judge(capa):
        res = 0
        # 각 심사대에서 수용가능한 인원들의 합을 구함.
        # 사실 정확히 무슨 의미인지는 잘 모르겠다
        for i in range(len(times)):
            res += capa // times[i]
        return res

    answer = 0
    while largest >= smallest:
        mid = (largest + smallest) // 2
        if judge(mid) >= n:
            largest = mid - 1
            answer = mid
        elif judge(mid) < n:
            smallest = mid + 1

    return answer
