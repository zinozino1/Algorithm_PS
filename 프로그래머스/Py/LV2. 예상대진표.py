# 단순 반복 구현
# 1,2,3,4,5,6,7,8이 다음 라운드에서 1,2,3,4 가 되는 것을 간과했다
# 자리수를 맞춰주기 위해 a,b에 1씩 더함

def solution(n, a, b):
    res = 0
    while a != b:
        a, b = (a+1)//2, (b+1)//2
        res += 1
    return res
