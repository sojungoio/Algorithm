def solution(slice, n):
    for i in range(1, 51):
        if slice * i / n >= 1:
             return i