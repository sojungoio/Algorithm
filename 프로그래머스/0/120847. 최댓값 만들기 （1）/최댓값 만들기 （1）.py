"""
1. 내림 차순으로 정렬..? 
2. 첫번째랑 두번째꺼만 꺼내서 곱하기???
3. 해보자
"""

def solution(numbers):
    answer = 0
    numbers.sort(reverse=True)
    for i in numbers[0 : 1]:
        for j in numbers[1 : 2]:
            answer = i * j
    return answer

"""
중첩 for문을 이용하지 않고 할 수 있는 방법이 있을까 

def solution(numbers):
    answer = 0
    numbers.sort(reverse=True)
    for i in numbers[0 : 2]:

"""