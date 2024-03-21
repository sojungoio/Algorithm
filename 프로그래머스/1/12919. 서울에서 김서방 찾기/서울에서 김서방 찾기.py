def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if seoul[i] in 'Kim':
            answer = '김서방은 ' + str(i) + '에 있다'
    return answer