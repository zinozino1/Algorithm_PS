# 실버5 - 30
# 그리디

n = "".join(list(map(str, sorted(list(input().strip()), reverse=True))))
if int(n) % 30 == 0:
    print(n)
else:
    print(-1)
