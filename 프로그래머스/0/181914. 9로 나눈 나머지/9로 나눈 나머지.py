def solution(number):
    answer = 0
    A = 0
    number = str(number)
    
    for i in number : 
        A += int(i)
        answer = A % 9
    
    return answer