# 정렬
# 삐꾸짓 해서 실수 함
def solution(citations):
    target = sorted(citations)
    max_cnt = -1e9
    for a in range(len(target)+1):
        low_cnt = 0
        for t in target:
            if a > t:
                low_cnt += 1
            else:
                break
        if len(target)-low_cnt >= a:
            if len(target)-low_cnt > max_cnt:
                max_cnt = a
    return max_cnt
