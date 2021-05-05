# 골드4-사냥꾼-이분탐색
# 구해야하는 것 : 잡을 수 있는 동물의 수
# 무엇을 이분탐색 타겟으로 잡을것인가? -> 동물은 픽스 시켜놓고 사대를 이분탐색 하자


def sol():

    N, M, L = map(int, input().split())
    sadae = list(map(int, input().split()))
    animals = [tuple(map(int, input().split())) for _ in range(M)]
    sadae.sort()
    animals.sort(key=lambda x: (x[0]))

    cnt = 0

    # 동물을 픽스, 반복문을 돌며 사대를 이분탐색 한다.
    for i in range(M):
        # 높이가 삼각형 범위 바깥이면 제외
        if animals[i][1] > L:
            continue

        # 특정 동물 좌표에 대해 커버할 수 있는 가장 가까운 양 옆의 사대 범위 구하기
        upper = animals[i][0]+L-animals[i][1]
        lower = animals[i][0]-L+animals[i][1]

        # 사대를 이분탐색하기 위한 두개의 포인터
        lt = 0
        rt = N-1
        # 이분탐색 실시
        while lt <= rt:
            mid = (lt+rt)//2
            # 해당 사대가 특정 동물의 임계값 내부라면 그 동물은 '사냥가능'
            if lower <= sadae[mid] <= upper:
                cnt += 1
                break
            elif sadae[mid] < lower:
                lt = mid + 1
            else:
                rt = mid - 1

    print(cnt)


sol()
