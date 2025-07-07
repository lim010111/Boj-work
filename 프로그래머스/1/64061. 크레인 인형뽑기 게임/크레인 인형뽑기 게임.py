def solution(board, moves):
    '''
    transpose board -> stacks
    '''
    result = 0
    n = len(board)

    stacks = [[board[r][c] for r in range(n) if board[r][c] != 0][::-1] for c in range(n)]

    stack_popped = []

    for move in moves:
        if not stacks[move - 1]:
            continue
        popped = stacks[move - 1].pop()
        
        if stack_popped and stack_popped[-1] == popped:
            stack_popped.pop()
            result += 1
        else:
            stack_popped.append(popped)
        

    return result * 2