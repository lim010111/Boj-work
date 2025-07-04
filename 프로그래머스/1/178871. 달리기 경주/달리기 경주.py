def solution(players, callings):
    '''
    어떤 선수가 바로 자기 앞의 선수를 추월했을 때-> 그 선수 이름 부르기 1회
    -> 앞의 선수와 스위칭
    -> 결과 리스트 반환
    '''
    
    rank_dict = {player:rank for rank, player in enumerate(players)}
    current_ranks = players[:]
    
    for calling in callings:
        passed = current_ranks[rank_dict[calling] - 1]
        taker = current_ranks[rank_dict[calling]]
        current_ranks[rank_dict[calling] - 1], current_ranks[rank_dict[calling]] = taker, passed
        
        rank_dict[taker] -= 1
        rank_dict[passed] += 1
        
    return current_ranks