def solution(my_string, alp):
    answer = ''
    for i in my_string:
        if alp in i:
            answer +=i.upper()
        else:
            answer +=i
    return answer