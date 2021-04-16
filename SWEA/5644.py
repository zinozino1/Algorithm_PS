# 시뮬레이션, 구현

def charge(ax, ay, bx, by):
    global result
    # a가 사용할 수 있는 충전기
    a_charge = []
    # b가 사용할 수 있는 충전기
    b_charge = []
    # 사용할 수 있는 충전기 찾기
    for i in range(A):
        x, y, C, P = AP[i]
        if abs(ax - x) + abs(ay - y) <= C:
            a_charge.append((i, P))
        if abs(bx - x) + abs(by - y) <= C:
            b_charge.append((i, P))

    # 성능이 높은 순으로 정렬
    a_charge.sort(key=lambda x: x[1], reverse=True)
    b_charge.sort(key=lambda x: x[1], reverse=True)

    # 같이쓰면 균등하게 분배 대신 -> 한사람이 몰아서 충전해도 결과는 같음
    # A가 먼저고르냐 B가 먼저고르냐에 따라 다름
    # A가 먼저 고름
    temp1 = 0
    for idx, P in a_charge:
        used = idx
        temp1 += P
        break
    for idx, P in b_charge:
        if idx != used:
            temp1 += P
            break
    # B가 먼저 고름
    temp2 = 0
    for idx, P in b_charge:
        used = idx
        temp2 += P
        break
    for idx, P in a_charge:
        if idx != used:
            temp2 += P
            break

    result += max(temp1, temp2)


# 무 상 우 하 좌
dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]


T = int(input())
for test_case in range(1, 1 + T):
    # 입력 받음
    M, A = map(int, input().split())
    route = [list(map(int, input().split())) for _ in range(2)]
    AP = [list(map(int, input().split())) for _ in range(A)]

    # 초기값
    Ax, Ay = 1, 1
    Bx, By = 10, 10
    result = 0
    charge(Ax, Ay, Bx, By)  # 충전
    for i in range(M):
        # 이동
        Ad, Bd = route[0][i], route[1][i]
        Ax, Ay = Ax + dx[Ad], Ay + dy[Ad]
        Bx, By = Bx + dx[Bd], By + dy[Bd]
        charge(Ax, Ay, Bx, By)  # 충전

    print('#{} {}'.format(test_case, result))
