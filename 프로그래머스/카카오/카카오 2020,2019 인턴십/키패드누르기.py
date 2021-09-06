# 단순 구현
def solution(numbers, hand):
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    left_pos = (3, 0)
    right_pos = (3, 2)
    res = ''
    for n in numbers:
        target_pos = None
        for i in range(4):
            for j in range(3):
                if n == board[i][j]:
                    target_pos = (i, j)
        if n == 1 or n == 4 or n == 7:
            left_pos = target_pos
            res += "L"
        elif n == 3 or n == 6 or n == 9:
            right_pos = target_pos
            res += "R"
        else:
            left_diff = abs(left_pos[0]-target_pos[0]) + \
                abs(left_pos[1]-target_pos[1])
            right_diff = abs(right_pos[0]-target_pos[0]) + \
                abs(right_pos[1]-target_pos[1])
            if left_diff < right_diff:
                left_pos = target_pos
                res += "L"
            elif left_diff > right_diff:
                right_pos = target_pos
                res += "R"
            else:
                if hand == "left":
                    left_pos = target_pos
                    res += "L"
                else:
                    right_pos = target_pos
                    res += "R"

    print(res)
    return res
