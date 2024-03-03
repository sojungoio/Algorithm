def solution(n, t):
    answer = n
    for i in range(t):
        answer *= 2
    return answer

"""
비트 연산자 
der solution(n, t):
    answer = n << t
    return answer
"""