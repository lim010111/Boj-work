'''
["frodo", "fradi", "crodo", "abc123", "frodoc"] -> ["fr*d*", "abc1**"]

[0, 0]
[frodo, 0] -> [frodo, abc123] 끝
[fradi, 0] -> [fradi abc123] 끝

중복 제거 위해 sorted 처리 후, 조합에 추가
'''

def solution(user_id, banned_id):
    combs = set()

    def is_banned_user(id, target_id):
        if len(id) != len(target_id):
            return False
        
        for i in range(len(id)):
                if target_id[i] == '*':
                    continue
                if id[i] != target_id[i]:
                    return False
        
        return True

    def fill_combs(current_comb, ban_idx):
        if ban_idx == len(banned_id):
            combs.add(tuple(sorted(current_comb[:])))
            return

        for i in range(len(user_id)):
            if user_id[i] in current_comb:
                continue

            if is_banned_user(user_id[i], banned_id[ban_idx]):
                current_comb.append(user_id[i])
                fill_combs(current_comb, ban_idx + 1)
                current_comb.pop()
    
                
    fill_combs([], 0)
    return len(combs)