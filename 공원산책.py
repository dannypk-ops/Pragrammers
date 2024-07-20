def solution(park, routine):
    answer = []

    for i, row in enumerate(park):
        for j, col in enumerate(row):
            if col == 'S':
                answer.append(i)
                answer.append(j)
    
    row_len = len(park)
    col_len = len(park[0])

    for data in routine:
        direction_len = data.strip().split()

        direction = direction_len[0]
        length = int(direction_len[1])

        if direction == 'E':
            if answer[1] + length >= col_len :
                continue
            else:
                for num in range(1, length+1):
                    if park[answer[0]][answer[1] + num] != 'X':
                        continue
                    else:
                        break
                else: 
                    answer[1] = answer[1] + length
        elif direction == 'W':
            if answer[1] - length < 0 :
                continue
            else:
                for num in range(1, length+1):
                    if park[answer[0]][answer[1] - num] != 'X':
                        continue
                    else:
                        break
                else:
                    answer[1] = answer[1] - length
        elif direction == 'S':
            if answer[0] + length >= row_len :
                continue
            else:
                for num in range(1, length+1):
                    if park[answer[0] + num][answer[1]] != 'X':
                        continue
                    else:
                        break
                else:
                    answer[0] = answer[0] + length
        elif direction == 'N':
            if answer[0] - length < 0 :
                continue
            else:
                for num in range(1, length+1):
                    if park[answer[0] - num][answer[1]] != 'X':
                        continue
                    else:
                        break
                else:
                    answer[0] = answer[0] - length
    return answer


