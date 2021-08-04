# 실버2 - 잃어버린 괄호
# 그리디

# n=50이므로 완전탐색 어려움 -> 부분집합으로 해야해서
# 쌍으로 괄호를 쳐야 하므로 dp도 어려움 -> 그리디

target = input().strip()
tmp = []

curr = ''
for t in target:
    if not t.isdecimal():
        tmp.append(curr)
        curr = ''
        if t == "-":
            curr += t
    else:
        curr += t
tmp.append(curr)

if tmp[0] == '':
    tmp.pop(0)
tmp = list(map(int, tmp))

ptr = 0
res = 0
while ptr <= len(tmp)-1:
    if tmp[ptr] >= 0:
        res += tmp[ptr]
        ptr += 1
    else:
        res += tmp[ptr]
        ptr += 1
        while True:
            if ptr == len(tmp):
                break
            if tmp[ptr] < 0:
                break
            res -= tmp[ptr]
            ptr += 1

print(res)
