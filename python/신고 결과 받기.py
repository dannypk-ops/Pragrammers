def solution(id_list, report, k):
    answer = []

    report_dict = {}
    reported_count = {}
    report_count = {}
    suspended_list = []

    for name in id_list:
        reported_count.update({name: 0})
        report_count.update({name:0})
    
    for value in report:
        value_list = value.strip().split()
        name_01 = value_list[0]
        name_02 = value_list[1]
        
        if name_01 in report_dict.keys():
            if name_02 not in report_dict[name_01]:
                report_dict[name_01].append(name_02)
            else:
                continue
        else:
            report_dict.update({name_01:[name_02]})

    for key, value in report_dict.items():
        for name in value:
            reported_count[name] += 1
            if reported_count[name] >= k:
                suspended_list.append(name)
                suspended_list = list(set(suspended_list))
    
    for key, value in report_dict.items():
        for name in suspended_list:
            if name in value:
                report_count[key] += 1

    answer = list(report_count.values())
    
    return answer