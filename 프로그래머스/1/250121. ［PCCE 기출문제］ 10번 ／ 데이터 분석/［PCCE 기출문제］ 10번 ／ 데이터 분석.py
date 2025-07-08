def solution(data, ext, val_ext, sort_by):
    '''
    ext: 최소 데이터 종류
    val_ext: ext를 기준으로 val_ext보다 작은 데이터만 필터링하기
    sort_by: 정렬 기준, 오름차순
    '''
    
    data_format = ["code", "date", "maximum", "remain"]
    for i, elem in enumerate(data_format):
        if ext == elem:
            ext_index = i
        
        if sort_by == elem:
            sort_by_index = i
        
    
    filtered_data = [d for d in data if d[ext_index] < val_ext]
    
    filtered_and_sorted_data = sorted(filtered_data, key=lambda d: d[sort_by_index])
    
    return filtered_and_sorted_data