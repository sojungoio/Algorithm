def solution(my_string, letter):
    answer = my_string.replace(letter, "")
    return answer

"""
다른 풀이법

def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if i != letter:
            answer += i
    return answer
    
"""