def solution(n, control):
    answer = 0
    for i in control:
        if i == 'w':
            n+=1
            answer = n 
        if i == 's':
            n-=1
            answer = n
        if i == 'd':
            n+=10
            answer = n 
        if i == 'a':
            n-=10
            answer = n
    return answer