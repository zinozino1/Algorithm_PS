def pick(board, num):
    curr = 0
    for j in range(len(board)):
        if board[j][num-1] != 0:
            curr = board[j][num-1]
            board[j][num-1] = 0
            break
    return curr


def solution(board, moves):
    stack = []
    cnt = 0
    for m in moves:
        curr = pick(board, m)
        if curr != 0:
            if stack and stack[-1] == curr:
                stack.pop()
                cnt += 2
            else:
                stack.append(curr)

    return cnt
