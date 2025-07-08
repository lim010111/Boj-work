def solution(X, Y):

    X_dict = {}
    Y_dict = {}
    
    for num in X:
        if num not in X_dict:
            X_dict[num] = 0
    
        X_dict[num] += 1
    
    for num in Y:
        if num not in Y_dict:
            Y_dict[num] = 0
    
        Y_dict[num] += 1
    
    
    common_num_dict = {}
    
    for num in X_dict:
        if num in Y_dict:
            common_num_dict[num] = min(X_dict[num], Y_dict[num])
    
    if not common_num_dict:
        return "-1"

    result = ""

    if list(common_num_dict.keys()) == ['0']:
        return '0'
    
    for num, count in common_num_dict.items():
        result += str(num) * count
    
    return ''.join(sorted(result, reverse=True))