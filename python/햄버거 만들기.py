def solution(ingredient):
    answer = 0
    ix = 0
    while True:
        if len(ingredient) > (ix + 3):
            if ingredient[ix:ix+4] == [1,2,3,1]:
                ingredient[ix:ix+4] = []
                answer += 1
                ix = 0 if ix < 3 else ix - 3
            else:
                ix += 1
        else:
            break
            
    return answer