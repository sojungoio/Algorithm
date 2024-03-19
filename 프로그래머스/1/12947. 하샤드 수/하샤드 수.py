def solution(x):
    answer = True
    ans = 0
    for i in str(x):
        ans += int(i)
        if x % ans == 0:
            answer = True
        else:
            answer = False
    return answer