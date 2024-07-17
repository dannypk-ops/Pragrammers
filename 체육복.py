def solution(n, lost, reserve):

    answer = 0
    reserve_lost = set(lost) & set(reserve)
    reserve_not_lost = list(set(reserve) - reserve_lost)
    pure_lost = list(set(lost) - reserve_lost)

    status = list()
    for i in range(n+1):
        status.append(1)
    
    for i in reserve_lost:
        status[i] = 1

    for i in reserve_not_lost:
        status[i] = 2

    for i in pure_lost:
        status[i] = 0
    

    for num in reserve_not_lost:
        if num != 1 and num != n:
            if status[num-1] == 0:
                status[num-1] = 1
            elif status[num+1] == 0:
                status[num+1] = 1
            else:
                continue
        else:
            if num == 1 and status[num+1] == 0:
                status[num+1] = 1
            elif num == n and status[num-1] == 0:
                status[num-1] = 1
            else:
                continue
    
    for idx, value in enumerate(status):
        if value != 0:
            answer += 1

    return answer - 1