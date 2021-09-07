# 문자열 + 구현

def replace(str):
    return str.replace("C#", "1").replace("D#", "2").replace("F#", "3").replace("G#", "4").replace("A#", "5")


def solution(m, musicinfos):
    m = replace(m)
    ans = []
    for idx, music in enumerate(musicinfos):
        start, end, title, melody = music.split(",")
        melody = replace(melody)
        start_h, start_m = int(start.split(":")[0]), int(start.split(":")[1])
        start = start_h * 60 + start_m
        end_h, end_m = int(end.split(":")[0]), int(end.split(":")[1])
        end = end_h * 60 + end_m
        duration = end - start
        target = (duration // len(melody)) * melody + \
            melody[:duration % len(melody)]

        if m in target:
            ans.append((title, duration, idx))

    if ans:
        ans.sort(key=lambda x: (-x[1], x[2]))
        return ans[0][0]
    else:
        return "(None)"
