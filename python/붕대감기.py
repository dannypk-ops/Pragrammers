def solution(bandage, health, attacks):
    answer = 0
    
    t, x, y = bandage[0], bandage[1], bandage[2]
    mhealth = health
    chealth = health
    ctime = 0
    
    for attack_info in attacks:
        time = attack_info[0]
        damage = attack_info[1]
        
        interval = (time - ctime) - 1
        ctime = time
        chealth = min(mhealth, chealth + interval * x + y * (interval // t)) - damage
        
        if chealth <= 0:
            return -1
        
    answer = chealth
    return answer
