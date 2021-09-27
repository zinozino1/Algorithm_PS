def solution(table, languages, preference):
    split_arr = []
    for t in table:
        split_arr.append(t.split(" "))
    max_score = -1e9
    candidate = "z"
    
    for s in split_arr:
        score = 0
        
        for i,lan in enumerate(languages):
            if lan in s:
                score += (5 - s.index(lan) + 1) * preference[i]
        
        if score > max_score:
            max_score = score
            candidate = s[0]
        elif score == max_score:
            if candidate > s[0]:
                candidate = s[0]
            
    return candidate