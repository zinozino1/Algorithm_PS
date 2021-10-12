# 골드5 - IPv6
# 문자열

target = input().strip()
splitted = target.split(":")

if splitted[0] == "":
    splitted = splitted[1:]
elif splitted[len(splitted)-1] == "":
    splitted = splitted[:len(splitted)-1]

none_empty = 0
for s in splitted:
    if s != "":
        none_empty += 1

res = ''
for s in splitted:
    if s == '':
        res += "0000:" * (8-none_empty)
    else:
        res += "0" * (4-len(s)) + s + ":"

print(res[:len(res)-1])
