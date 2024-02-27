import numpy

def solution(numbers):
    answer = 0
    # for aver in numbers:
    #     answer += aver / len(numbers)
    answer = numpy.mean(numbers)
    return answer
    