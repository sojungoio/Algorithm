def solution(n, t):
    answer = n
    # for i in range(t):
    #     answer *= 2

    # heohy: for 순회 시, 사용하지 않는 값은 _(underbar) 로 표현 해야함. 코드 가독성을 위한 convention.
    for _ in range(t):
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
