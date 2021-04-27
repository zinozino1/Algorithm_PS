
def sol():
    global min_cnt

    # 고장나지 않은 버튼으로 만들 수 있는 모든 경우의 수 구함
    def dfs(L, tot):
        global min_cnt

        if L != 0:
            tmp = int("".join(map(str, tot)))
            # + or - 버튼 누른 횟수 + 숫자 버튼 누른 횟수
            cnt = abs(tmp - n) + L

            if cnt < min_cnt:
                min_cnt = cnt
        # 타겟넘버보다 크게 만들고 '-'버튼으로 이동시킬 수 있으므로 타겟넘버보다 길이 1 크게 만듦
        if L == len(str(n)) + 1:
            return
        else:
            for s in range(len(available_btn)):
                tot.append(available_btn[s])
                dfs(L + 1, tot)
                tot.pop()

    n = int(input())
    m = int(input())
    min_cnt = 1e9
    broken_btn = []
    available_btn = []
    # 고장난 버튼 없는 경우 입력 안 받음
    if m == 0:
        available_btn = list(set(range(10)))
    # 있는 경우 입력 받음
    else:
        broken_btn = list(map(int, input().split()))
        available_btn = list(set(range(10)) - set(broken_btn))

    dfs(0, [])
    # 100에 근접한 숫자이면 숫자버튼 누르는 거보다 +,- 버튼 누르는 게 더 좋으므로 비교작업
    if abs(n - 100) < min_cnt:
        print(abs(n - 100))
    else:
        print(min_cnt)


sol()
