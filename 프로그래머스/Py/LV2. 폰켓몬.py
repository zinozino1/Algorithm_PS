# 완전탐색이 아님..
# set으로 중복 제거하면 쉽게 해결 가능하잖아

def solution(nums):
    t = set(sorted(nums))
    if len(t) >= len(nums)//2:
        return len(nums)//2
    else:
        return len(t)
