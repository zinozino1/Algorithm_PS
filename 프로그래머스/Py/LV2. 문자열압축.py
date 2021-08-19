# 스택 활용하려다 그냥 단순 반복으로 해결
# 약간 까다로웠음

def solution(s):

    stack = []
    min_len = 1e9

    if len(s) == 1:
        return 1

    for le in range(1, (len(s)//2)+1):
        res = ''
        prev = s[:le]
        curr = ''
        cnt = 1
        for i in range(le, len(s), le):
            curr = s[i:i+le]
            if prev == curr:
                cnt += 1
            else:
                if cnt == 1:
                    res += prev
                else:
                    res += str(cnt)+prev
                cnt = 1
            prev = curr

        if len(curr) < len(prev):
            res += curr
            break
        else:
            if cnt == 1:
                res += curr
            else:
                res += str(cnt)+curr

        if len(res) < min_len:
            min_len = len(res)

    return min_len
