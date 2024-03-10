
# import numpy

# def solution(numbers):
#     answer = 0
#     # for aver in numbers:
#     #     answer += aver / len(numbers)
#     answer = numpy.mean(numbers)
#     return answer


"""
heohy
간단한 연산 함수를 작성하기 위해 numpy 를 import 하는 것은 자원 측면에서 비효율적 이므로,
파이썬 기본 내장 라이브러리로 함수를 작성 하는 게 좋다.
"""
def solution(numbers):
    return sum(numbers) / len(numbers)