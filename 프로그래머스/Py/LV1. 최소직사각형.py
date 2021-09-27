# 구현

def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][1] > sizes[i][0]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    row, col = -1e9, -1e9
    for size in sizes:
        row = max(size[0], row)
        col = max(size[1], col)
    return row * col
