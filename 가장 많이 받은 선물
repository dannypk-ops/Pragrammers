def solution(friends, gifts):
    
    gift_relation = {}
    gift_index = {}
    result = {}

    for name_01 in friends:
        gift_relation[name_01] = {}
        gift_index[name_01] = [0, 0, 0]
        result[name_01] = 0
    
    for name_01 in friends:
        for name_02 in friends:
            gift_relation[name_01].update({name_02 : 0})

    for data in gifts:
        data_list = data.split()
        give = data_list[0]
        given = data_list[1]

        gift_relation[give][given] += 1
    
    for (name_01, dic) in gift_relation.items():
        for name_02, count in dic.items():
            gift_index[name_01][0] += count
            gift_index[name_02][1] += count

    for index_list in gift_index.values():
        index_list[2] = index_list[0] - index_list[1]

    for name_01 in friends:
        for name_02 in friends:
            if name_01 == name_02:
                continue
            else:
                if gift_relation[name_01][name_02] > gift_relation[name_02][name_01]:
                    result[name_01] += 1
                elif gift_relation[name_01][name_02] < gift_relation[name_02][name_01]:
                    continue
                else:
                    if gift_index[name_01][2] > gift_index[name_02][2]:
                        result[name_01] += 1
                    else:
                        continue
    
    return max(result.values())
