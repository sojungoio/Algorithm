def solution(n):
    answer = 0
    i = n ** (1/2)
    if i != int(i):
        answer = -1
    else:
        answer = (i+1) ** 2
    return answer