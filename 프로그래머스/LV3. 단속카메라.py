# 그리디 - 아이디어 생각해내는게 매우 어려움
# 1. 진출 차수 기준으로 오름차순 정렬
# 2. 처음 카메라의 위치를 -30001로 설정
# 3. 카메라의 위치와 경로의 진입 차수를 비교하여 진입 차수가 더 작다면 카메라를 설치. -> camera = route[1]로 설정
# * 진출차수 기준으로해야 이미 지나온 경로인지 알 수 있다.

def solution(routes):
    res = 0
    routes.sort(key=lambda x: x[1])
    camera = -30001
    for r in routes:
        if camera < r[0]:
            camera = r[1]
            res += 1
    return res
