# 문자열 스택

# 내 풀이 -> stack을 활용하여 풀려 했으나 못 품

from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str):
        stack = []
        res = ''
        tmp = []
        for char in s:
            if stack and char in stack:
                while stack and stack[-1] != char:
                    tmp.append(stack.pop())
                stack.pop()
                tmp.append(char)
                min_char = min(tmp)
                stack.append(min_char)
                while tmp:
                    curr = tmp.pop()
                    if curr not in stack:
                        stack.append(curr)

            else:
                stack.append(char)

        return "".join(stack)


# 답 -> 스택 + 카운터 활용 개어려움


class Solution:
    def removeDuplicateLetters(self, s: str):
        stack, counter, seen = [], Counter(s), set()

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue

            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return "".join(stack)
