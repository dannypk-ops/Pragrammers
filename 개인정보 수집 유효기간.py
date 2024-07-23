def solution(today, terms, privacies):
    answer = []
    
    today = today.split('.')
    today_info = list(map(int, today))
    
    term_dict = {}
    for data in terms:
        term_list = data.split()
        term_dict[term_list[0]] = int(term_list[1])
    
    for idx, data in enumerate(privacies):
        data_list = data.split()
        
        date = data_list[0].split('.')
        date_info = list(map(int, date))
        term = term_dict[data_list[1]]
        
        k = date_info[1] + term
        if k <= 12:
            delta_year = 0
            month = k
        else:
            if k % 12 == 0:
                delta_year = k //12 - 1
                month = 12
            else:
                delta_year = k // 12
                month = k % 12
        date_info[0] += delta_year
        date_info[1] = month
        
        if date_info[0] < today_info[0]:
            answer.append(idx + 1)
        elif (date_info[0] == today_info[0]) and (date_info[1] < today_info[1]):
            answer.append(idx + 1)
        elif (date_info[0] == today_info[0]) and (date_info[1] == today_info[1]) and (date_info[2] <= today_info[2]):
            answer.append(idx + 1)
        else:
            continue
        
    return sorted(answer)
