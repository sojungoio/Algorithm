def solution(order):
    answer = 0
    order = str(order)
    
    for i in order:
        if int(i) % 3 == 0 and int(i) != 0 :
            answer +=1
    return answer