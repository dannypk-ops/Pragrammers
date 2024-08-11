def solution(survey, choices):
    answer = ''
    
    total_score = {'R':0, 'T':0,
                  'C':0, 'F':0,
                  'J':0, 'M':0,
                  'A':0, 'N':0}
    
    for item, point in zip(survey, choices):
        no = item[0]
        yes = item[1]
        
        if point <= 3:
            total_score[no] += (4 - point)
        elif point >= 5:
            total_score[yes] += (point - 4)
        else:
            continue
    
    if total_score['R'] > total_score['T']:
        answer += 'R'
    elif total_score['R'] < total_score['T']:
        answer += 'T'
    else:
        answer += 'R'
    
    if total_score['C'] > total_score['F']:
        answer += 'C'
    elif total_score['C'] < total_score['F']:
        answer += 'F'
    else:
        answer += 'C'
        
    if total_score['J'] > total_score['M']:
        answer += 'J'
    elif total_score['J'] < total_score['M']:
        answer += 'M'
    else:
        answer += 'J'
        
    if total_score['A'] > total_score['N']:
        answer += 'A'
    elif total_score['A'] < total_score['N']:
        answer += 'N'
    else:
        answer += 'A'
                    
    return answer