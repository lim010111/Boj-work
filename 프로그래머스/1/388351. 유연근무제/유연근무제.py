def solution(schedules, timelogs, startday):
    '''
    출근 희망 시각 + 10분까지 제한 -> 상품
    토, 일은 대상 제외
    매일 1번씩 가능
    시간: 시 * 100 + 분
    
    상품을 받을 직원의 수
    
    scheduels: i번째 직원이 설정한 출근 희망 시각
    timelogs: i번째 직원, day 당 출근한 시각 -> 7개 고정 배열이 주어지므로, 무조건 1주일, 휴일 2개는 빼도 될듯
    startday: 뺄 휴일 계산
    
    출근 로직 -> if schedule + 10 >= timelog
    *** if schedule + 10 % 100 >= 60:
            100 더하고 60 빼기
    
    뺄 휴일 계산하기 -> 
        if startday == 1:
            timelog = timelog[:7 - startday - 1] + timelog[7 - startday + 1:]
    '''
    for i, schedule in enumerate(schedules):
        if schedule % 100 >= 50:
            schedules[i] = schedule + 100 - 50
        
        else:
            schedules[i] += 10
            
    if startday == 7:
        timelogs = [logs[1:6] for logs in timelogs]
    else:       
        timelogs = [timelog[:7 - startday - 1] + timelog[7 - startday + 1:] for timelog in timelogs]
    deserved = [True] * len(schedules)
    for i, timelog in enumerate(timelogs):
        set_time = schedules[i]
        for time in timelog:
            if set_time < time:
                deserved[i] = False
                break
                
    return deserved.count(True)
    