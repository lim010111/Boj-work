def solution(ingredient):
    burgers = 0
    stack = []
    
    for elem in ingredient:
        stack.append(elem)
        if stack[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                stack.pop()
            burgers += 1
            
    return burgers