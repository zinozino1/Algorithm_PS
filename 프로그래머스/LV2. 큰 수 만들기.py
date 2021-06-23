# 옛날에 풀었던건데 막혔음
# 기본적으로 스택 + 그리디 활용

def solution(number, k):
    stack = []
    for n in number:
      # 스택에 넣기 전에 넣으려는 값보다 작은 수가 있는지 검사
      # 수를 pop할 때마다 제거 카운트 감소
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)
    # 제거 카운트가 남아있다면 슬라이싱
    if k != 0:
        stack = stack[:-k]
    return "".join(stack)
