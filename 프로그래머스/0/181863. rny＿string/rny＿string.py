def solution(rny_string):
    answer = ''
    for i in rny_string:
        if 'm' == i:
            i = 'rn'
        answer+=i
            
    return answer