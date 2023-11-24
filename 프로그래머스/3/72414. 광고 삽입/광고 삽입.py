def solution(play_time, adv_time, logs):
    answer = 0

    dp = [0 for _ in range(time_to_sec('100:00:00'))]

    play_time_sec = time_to_sec(play_time)
    adv_time_sec = time_to_sec(adv_time)
    for log in logs:
        log_start, log_end = log.split("-")
        log_start_sec = time_to_sec(log_start)
        log_end_sec = time_to_sec(log_end)

        dp[log_start_sec] += 1
        dp[log_end_sec] -= 1 
    
    for i in range(1, len(dp)):
        dp[i] += dp[i-1]
    for i in range(1, len(dp)):
        dp[i] += dp[i-1]
    
    mx_value = 0
    start = 0
    logs.sort()

    for i in range(adv_time_sec-1, play_time_sec):
        result = dp[i] - dp[i-adv_time_sec]
        if i >= adv_time_sec:
            if mx_value < result:
                mx_value = result
                start = i-adv_time_sec+1

        else:
            mx_value = dp[i]
            start = i-adv_time_sec+1            

    answer = sec_to_time(start)
    return answer

def time_to_sec(s: str) :
    splited = s.split(":")

    return int(splited[0]) * 3600 + int(splited[1]) * 60 + int(splited[2]) 

def sec_to_time(s: int): 
    sec = s % 60
    s //= 60
    min = s % 60
    s //= 60
    hour = s
    return str(hour).zfill(2) + ":" + str(min).zfill(2) + ":" + str(sec).zfill(2)
