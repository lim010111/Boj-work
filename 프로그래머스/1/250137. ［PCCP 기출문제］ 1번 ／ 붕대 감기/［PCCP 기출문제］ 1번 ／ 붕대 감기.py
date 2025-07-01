from typing import List
from collections import deque

def solution(bandage: List[int], health: int, attacks: List[List[int]]) -> int:
    heal_duration, heal, bonus = bandage
    current_health = health
    attacks_q = deque(attacks)
    
    heal_t = 0
    attack_t = 0
    attack_duration, damage = attacks_q.popleft()
    while True:
        heal_t += 1
        attack_t += 1
        for i in range(len(attacks_q)):
            attacks_q[i][0] -= 1
            
        print(current_health, attack_duration, attack_t)
        if attack_duration <= 0 or attack_t == attack_duration:
            current_health -= damage
            if current_health <= 0:
                return -1
            
            if attacks_q:
                attack_duration, damage = attacks_q.popleft()
            else:
                break
                
            heal_t = 0
            attack_t = 0
            continue
        
        current_health += heal
        
        if heal_t == heal_duration:
            current_health += bonus
            heal_t = 0
            
        if current_health > health:
            current_health = health
            
    return current_health
        