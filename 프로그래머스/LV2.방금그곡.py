# 단순구현 + 문자열
# "#"조건 + 반례 때문에 상당히 오래걸림

def solution(m, musicinfos):
    ans_cnt = len(musicinfos)
    res = []
    for idx, music in enumerate(musicinfos):
        start, end, title, melody = music.split(",")[0], music.split(
            ",")[1], music.split(",")[2], music.split(",")[3]
        start_h, start_m = start.split(":")[0], start.split(":")[1]
        end_h, end_m = end.split(":")[0], end.split(":")[1]
        time_diff = (int(end_h)-int(start_h))*60+int(end_m)-int(start_m)
        new_melody = ''
        i, cnt = 0, 0
        while True:
            if cnt == time_diff:
                break
            new_melody += melody[i % len(melody)]
            if melody[i % len(melody)] != "#":
                cnt += 1
            i += 1
        if melody[i % len(melody)] == "#":
            new_melody += "#"

        for i in range(len(new_melody)-len(m)+1):
            if i != len(new_melody)-len(m):
                if m == new_melody[i:i+len(m)] and new_melody[i+len(m)] != "#":
                    res.append((idx, title, time_diff))
                    break
            else:
                if m == new_melody[i:i+len(m)]:
                    res.append((idx, title, time_diff))
                    break

    if not res:
        return "(None)"
    else:
        res.sort(key=lambda x: (-x[2], x[0]))
        return res[0][1]


# 고수 풀이 -> replace활용


def shap_to_lower(s):
    s = s.replace('C#', 'c').replace('D#', 'd').replace(
        'F#', 'f').replace('G#', 'g').replace('A#', 'a')
    return s


def solution(m, musicinfos):
    answer = [0, '(None)']   # time_len, title
    m = shap_to_lower(m)
    for info in musicinfos:
        split_info = info.split(',')
        time_length = (int(split_info[1][:2])-int(split_info[0][:2])) * \
            60+int(split_info[1][-2:])-int(split_info[0][-2:])
        title = split_info[2]
        part_notes = shap_to_lower(split_info[-1])
        full_notes = part_notes * \
            (time_length//len(part_notes)) + \
            part_notes[:time_length % len(part_notes)]
        if m in full_notes and time_length > answer[0]:
            answer = [time_length, title]
    return answer[-1]
