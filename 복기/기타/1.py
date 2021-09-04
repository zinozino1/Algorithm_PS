# LG 전자 sample test 1번

def solution():
    n, t = map(int, input().split())
    worker = [tuple(map(int, input().split())) for _ in range(n)]
    expected_pos = [init_pos + speed * t for init_pos, speed in worker]
    group = {}

    for i in range(n-2, -1, -1):
        if expected_pos[i] > expected_pos[i+1]:
            expected_pos[i] = expected_pos[i+1]

    for pos in expected_pos:
        group[pos] = group.get(pos, 0)+1

    return len(group.keys())


solution()
