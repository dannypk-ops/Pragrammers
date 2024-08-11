def solution(board, moves):
    answer = 0
    
    bascket = []
    board_len = len(board[0])
    
    for move in moves:
        for idx in range(board_len):
            if board[idx][move-1] != 0:
                bascket.append(board[idx][move-1])
                board[idx][move-1] = 0
                if (len(bascket) >= 2) and (bascket[-1] == bascket[-2]):
                    bascket.pop()
                    bascket.pop()
                    answer += 2
                break
    return answer