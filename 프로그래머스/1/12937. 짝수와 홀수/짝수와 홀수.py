def solution(num):
    answer = ''
    while True:
        if num % 2 == 0:
            answer = 'Even'
        elif num == 0:
            answer = 'Even'
        else:
            answer = 'Odd'
        break    
    return answer