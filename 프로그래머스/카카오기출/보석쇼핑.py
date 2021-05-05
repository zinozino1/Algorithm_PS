# 첫번째 시도 - 이분탐색
# 최대 10만이므로 nlogn인 이분탐색으로 풀었으나 TLE

def solution(gems):
    dic = dict()

    for i in range(len(gems)):
        dic[gems[i]] = dic.get(gems[i], 0)+1

    minN = 1e9
    ans = []

    for i in range(len(gems)):
        lt = i
        rt = len(gems)-1
        while lt <= rt:
            mid = (lt+rt) // 2
            if len(set(gems[i:mid+1])) >= len(set(dic.keys())):
                rt = mid - 1
                if mid-i < minN:
                    minN = mid-i
                    ans = []
                    ans.append(i+1)
                    ans.append(1+mid)
            else:
                lt = mid + 1

    return ans

# 두번째 시도 - 투포인터
# o(n)으로 해결 가능


def solution2(gems):
    # 보석 종류
    size = len(set(gems))
    dic = {gems[0]: 1}
    ans = [1, len(gems)]
    start, end = 0, 0
    while(start < len(gems) and end < len(gems)):
        if len(dic) != size:
            end += 1
            if end >= len(gems):
                break
            dic[gems[end]] = dic.get(gems[end], 0) + 1
        else:
            if end - start < ans[1] - ans[0]:
                ans = [start + 1, end + 1]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1
    return ans
