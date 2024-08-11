def solution(k, score):
    answer = []
    Hall_of_Fame = []

    for idx, item in enumerate(score):
        if idx < k:
            Hall_of_Fame.append(item)
            Hall_of_Fame.sort(reverse=True)
            answer.append(Hall_of_Fame[idx])
        else:
            min_item = Hall_of_Fame[k-1]
            min_index = k - 1
            if min_item < item:
                Hall_of_Fame.pop()
                Hall_of_Fame.append(item)
                Hall_of_Fame.sort(reverse=True)
                answer.append(Hall_of_Fame[k-1])
            else:
                answer.append(min_item)
    return answer

k = 3
score = [10, 100, 20, 150, 1, 100, 200]
print(solution(k, score))
