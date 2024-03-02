def solution(my_string):
    answer = ''
    for str in my_string:
        answer = str + answer
    return answer

"""
문자열이 있다면?
a, b, c, d 이런 식으로 for 반복문을 돌고 
새 문자열 = a + 새 문자열('')
새 문자열 = b + 새 문자열('a')
새 문자열 = c + 새 문자열('ba')
새 문자열 = d + 새 문자열('cba')
이런식으로 된다. 
"""