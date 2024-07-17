def solution(X, Y):
    answer = ''
    
    dict_x = {
        '0' : 0,
        '1' : 0,
        '2' : 0,
        '3' : 0,
        '4' : 0,
        '5' : 0,
        '6' : 0,
        '7' : 0,
        '8' : 0,
        '9' : 0,
    }
    dict_y = {
        '0' : 0,
        '1' : 0,
        '2' : 0,
        '3' : 0,
        '4' : 0,
        '5' : 0,
        '6' : 0,
        '7' : 0,
        '8' : 0,
        '9' : 0,
    }

    for num in X:
        dict_x[num] += 1
    for num in Y:
        dict_y[num] += 1

    common = []
    
    # for num in X:
    #     if num in Y:
    #         common.append(num)
    #         Y = Y.replace(num,"",1)

    for num in '0123456789':
        dist = min(dict_x[num], dict_y[num])
        if dist != 0:
            for count in range(dist):
                common.append(num)


    common.sort(reverse=True)
    
    if len(common) == 0:
        return "-1"
    elif common[0] == '0':
        return '0'
    else:
        for num in common:
            answer += num
        
    return answer