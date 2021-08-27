# dfs + 문자열
# itertools에 목매지 말것
# itertools는 확실할 떄 쓰자. 애매하면 dfs 트리를 그려


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def dfs(L, tot):
            if L == len(digits):
                res.append(tot)
                return
            else:
                for i in range(len(dic[digits[L]])):
                    dfs(L+1, tot+dic[digits[L]][i])
        dfs(0, '')
        return res
