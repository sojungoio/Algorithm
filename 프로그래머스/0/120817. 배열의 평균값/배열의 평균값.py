def solution(numbers):
    answer = 0
    for aver in numbers:
        answer += aver / len(numbers)
    return answer