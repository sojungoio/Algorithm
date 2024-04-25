def solution(strArr):
    answer = []
    for i in range(0, len(strArr)):
        print(i)
        if i % 2 == 0:
            answer.append(str(strArr[i]).lower())
        else:
            answer.append(str(strArr[i]).upper())
    return answer