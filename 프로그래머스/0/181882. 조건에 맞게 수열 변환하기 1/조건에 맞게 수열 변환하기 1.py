def solution(arr):
    answer = []
    for i in arr :
        if i >= 50 and i % 2 == 0 :
            answer.append(i // 2)
        elif i < 50 and i % 2 == 1 : 
            answer.append(i * 2)
        else :
            answer.append(i)
    return answer

# import math

# def solution(arr):
#     answer = []
#     for i in arr:
#         if i > 50 and i % 2 == 0:
#             a = math.floor(i/2)
#             answer.append(a)
#         elif i < 50 and i % 2 != 0:
#             a = i*2
#             answer.append(a)
#         else : 
#             a = i
#             answer.append(a)
#     return answer