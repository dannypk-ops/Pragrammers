num_pad = [
           [1,2,3],
           [4,5,6],
           [7,8,9],
           ['*', 0, '#']
          ]

def return_index(num):
    j = 0
    if isinstance(num, int):
        if num >= 1 and num <= 3:
            i = 0
        elif num >= 4 and num <= 6:
            i = 1
        elif num >= 7 and num <= 9:
            i = 2
        else:
            i = 3
            j = 1
        if j == 0:
            for index, number in enumerate(num_pad[i]):
                if number == num:
                    j = index
                    break
    else:
        i = 3
        if num == '*':
            j = 0
        else:
            j = 2
                    
    return (i, j)

def solution(numbers, hand):
    answer = ''
    left , right, dist_left, dist_right = '*', '#', 0, 0
    
    for num in numbers:
        if num not in [2, 5, 8, 0]:
            if num in [1,4,7]:
                answer += 'L'
                left = num
            else:
                answer += 'R'
                right = num
        else:
            index_num = return_index(num)
            index_left = return_index(left)
            index_right = return_index(right)
            
            dist_left = abs(index_num[0] - index_left[0]) + abs(index_num[1] - index_left[1])
            dist_right = abs(index_num[0] - index_right[0]) + abs(index_num[1] - index_right[1])
            
            if dist_left < dist_right:
                answer += 'L'
                left = num
            elif dist_left > dist_right:
                answer += 'R'
                right = num
            else:
                if hand == 'left':
                    answer += 'L'
                    left = num
                else:
                    answer += 'R'
                    right = num
    return answer