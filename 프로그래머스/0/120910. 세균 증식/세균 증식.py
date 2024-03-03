def solution(n, t):
    answer = n
    for i in range(t):
        answer *= 2
    return answer

"""
비트 연산자 
def solution(n, t):
    answer = n << t
    return answer
    
제곱근 이용하기
def solution(n, t):
    answer = 2 ** t * n 
    return = answer
"""