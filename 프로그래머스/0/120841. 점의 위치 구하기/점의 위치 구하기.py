def solution(dot):
    
#     if dot[0]>0:
#         if dot[1]>0:
#             answer = 1
#         elif dot[0]<0:
#             answer = 4
#     elif dot[0] < 0:
#         if dot[1] > 0:
#             answer = 2
#         elif dot[1] < 0:
#             answer = 3
    if dot[0] >0 and dot[1] > 0:
        return 1
    elif dot[0] < 0 and dot[1] >0:
        return 2
    elif dot[0] <0 and dot[1] < 0:
        return 3
    elif dot[0] > 0 and dot[1] <0:
        return 4