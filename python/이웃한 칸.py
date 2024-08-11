def solution(board, h, w):
    answer = 0

    length = len(board)
    color = board[h][w]

    result = []
    result.append(board[h-1][w] if h != 0 else "")
    result.append(board[h][w-1] if w != 0 else "")
    result.append(board[h+1][w] if h != length else "")
    result.append(board[h][w+1] if w != length else "")

    for c in result:
        if c == color:
            answer += 1

    return answer
