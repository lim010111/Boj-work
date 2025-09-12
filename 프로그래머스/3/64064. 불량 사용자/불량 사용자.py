def solution(user_id, banned_id):
    combs = set()

    # 백트레킹:
    # []랑 현재 index 넣고, 현재 인덱스에 맞는 banned_id랑 비교하며 재귀로 [] 채우기
    def fill_combs(current_comb, depth, ban_idx):
        if ban_idx == len(banned_id):
            combs.add(tuple(sorted(current_comb[:])))
            return

        for i in range(len(user_id)):
            if user_id[i] in current_comb:
                continue
            # TODO: banned_id[ban_idx]와 user_id[i]의 fit 판단
            if is_banned_user(user_id[i], banned_id[ban_idx]):
                current_comb.append(user_id[i])
                fill_combs(current_comb, depth + 1, ban_idx + 1)
                current_comb.pop()
    
    def is_banned_user(id, covered_id):
        if len(id) != len(covered_id):
            return False
        
        for i in range(len(id)):
                if covered_id[i] == '*':
                    continue
                if id[i] != covered_id[i]:
                    return False
        
        return True
                
    fill_combs([], 0, 0)
    return len(combs)