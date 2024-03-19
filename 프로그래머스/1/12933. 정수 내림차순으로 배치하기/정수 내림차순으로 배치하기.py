def solution(n):
    ans = list(str(int(n)))
    ans.sort(reverse = True)
    return int("".join(ans))