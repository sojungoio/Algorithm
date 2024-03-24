def solution(my_string):
    i = ("a,e,i,o,u")
    answer = ''
    for j in my_string:
        if j not in i:
            answer+=j
    return answer