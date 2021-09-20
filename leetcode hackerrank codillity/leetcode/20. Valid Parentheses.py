# 풀이시간 : 5분


# 내 풀이 -> 간단하게 스택 활용
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif c == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif c == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
