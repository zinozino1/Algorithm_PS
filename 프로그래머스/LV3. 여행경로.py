def solution(tickets):
    global answer_cnt, answer
    # 가능한 경로가 2개 이상일 경우 알파벳 순서므로 정렬해줌
    tickets.sort(key=lambda x: (x[1], x[0]))
    # 중복 체크
    check = [0]*len(tickets)
    # 답이 여러개가 나올 수 있는데 그 중 하나만 선택하기 위함
    answer_cnt, answer = 0, None

    def dfs(L, start, end, res):
        global answer_cnt, answer
        # 여행이 끝났을 때
        if L == len(tickets) and answer_cnt == 0:
            answer_cnt += 1
            answer = res[:]
            return
        else:
            for i in range(len(tickets)):
                if check[i] == 0 and end == tickets[i][0]:
                    check[i] = 1
                    res.append(tickets[i][1])
                    # start와 end를 업데이트해서 다시 재귀
                    dfs(L+1, tickets[i][0], tickets[i][1], res)
                    check[i] = 0
                    # 백트래킹
                    res.pop()

    dfs(0, "", "ICN", ["ICN"])
    return answer
