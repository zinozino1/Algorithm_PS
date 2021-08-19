def solution(begin, target, words):
    global minN
    minN = 1e9
    # 중복 방치 체크 리스트
    check = [0]*len(words)

    # 모든 경우 탐색
    def dfs(L, res, begin, prev):
        global minN
        # begin = 계속 변하는 변수 -> target과 일치하면 리턴
        if begin == target:
            if L < minN:
                minN = L
            return
        # 모든 단어 탐색
        for i in range(len(words)):
            # 한 글자만 바꿀 수 있음
            match_flag = False
            match_cnt = 0
            for j in range(len(words[i])):
                if words[i][j] == begin[j]:
                    match_cnt += 1
            # i 번째 사용된 원소는 중복되어 사용되지 못하게 막기
            if check[i] == 0 and len(words[i]) - match_cnt == 1:
                check[i] = 1
                prev = begin  # 비교 실패했을 경우 이전 단어로 백트래킹 하기 때문에 prev 설정
                dfs(L+1, res+words[i], words[i], prev)
                check[i] = 0

    dfs(0, '', begin, begin)

    return minN if minN != 1e9 else 0
