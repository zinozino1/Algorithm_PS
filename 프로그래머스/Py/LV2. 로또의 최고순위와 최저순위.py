def solution(lottos, win_nums):

    min = 0
    max = 0

    for l in lottos:
        if l in win_nums:
            max += 1

    if max == 0 and lottos.count(0) == 0:
        return [6, 6]
    min = 7 - (max + lottos.count(0))
    if max != 0:
        max = 7 - max
    else:
        max = 6

    return [min, max]
