"""
1. 배열안에 있는걸 하나하나 머쓱이 키랑 비교하기 
2. 그리고 머쓱이 키 보다 큰 숫자를 세기.
"""

def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            # answer += array.count(i)
            answer += 1
    return answer