import math

def solution(money):
    answer = []
    answer = [math.floor(money/5500), money%5500]
    return answer