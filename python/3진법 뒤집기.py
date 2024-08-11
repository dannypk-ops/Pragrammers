def solution(n):
    answer = ""
    
    a = n // 3
    b = n % 3
    answer += str(b)
    
    while True:
        if a == 0:
            break
        b = a % 3
        a = a // 3
        answer += str(b)
    
    length = len(answer)
    num = 0
    
    i = 0
    for n in reversed(answer):
        num += int(n) * (3 ** i)
        i += 1
    
    return num