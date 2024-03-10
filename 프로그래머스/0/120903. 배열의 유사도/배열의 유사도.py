def solution(s1, s2):
    answer = 0
    for i in s2:
        for j in s1:
            if i == j:
                answer +=1
    return answer


"""
heohy
중첩 된 블럭을 사용하는 코드는 가독성을 떨어뜨리는 안티 패턴이므로 지양해야 한다
이중 중첩 까지는 상황에 따라 허용 되지만 삼중 중첩문은 절대 X.
"""
def solution(s1, s2):
    answer = 0
    for s1_item in s1:
        if s1_item in s2:
            answer += 1

    return answer
