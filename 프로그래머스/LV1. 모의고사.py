# 완전탐색
# 멍청한짓 함. 가장 큰 친구 외에는 res배열에 들어갈 필요가 없는데 나머지도 넣으려해서 오류났음
# max값 한 번 정해놓으면 max값과 같은 친구를 넣으면 된다.

def solution(answers):

    peoples = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    tmp = []
    res = []
    for i in range(3):
        cnt = 0
        for j in range(len(answers)):
            if answers[j] == peoples[i][j % len(peoples[i])]:
                cnt += 1
        tmp.append(cnt)
    maxN = tmp[0]
    for x in tmp:
        if x > maxN:
            maxN = x
    for i in range(3):
        if tmp[i] == maxN:
            res.append(i+1)

    return res


# 그렇다면 나머지도 넣고싶다면?
# 아마 이중 반복문을 쓰면 될 것이다
# 첫번째 루프에서 max값 정해놓고 두번째 루프에서 그 맥스값과 동일한 친구들을
# res배열에 넣어주면 됨
