def solution(n, words):
    answer = []

    pre_word = ""
    word_list = []
    
    for index, word in enumerate(words):
        if index == 0:
            pre_word = word
            word_list.append(word)
            continue
        
        if (word[0] == pre_word[-1]) and (word not in word_list):
            word_list.append(word)
            pre_word = word
        else:
            number = n if (index + 1) % n == 0 else  (index + 1) % n
            a = (index + 1) // n
            sequence = a if (index + 1) % n == 0 else a + 1
            
            answer.append(number)
            answer.append(sequence)
            
            return answer
        
    answer.append(0)
    answer.append(0)

    return answer