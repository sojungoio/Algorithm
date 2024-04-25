def solution(myString, pat):
    answer = 0
    answer2 = ''
    for i in myString:
        if i == 'A':
            i = 'B'
            answer2 += i
        else:
            i = 'A'
            answer2 +=i
    if pat in answer2:
        answer = 1
    else:
        answer = 0
    return answer