def solution(arr1, arr2):
    answer = 0
    a = 0
    b = 0
    for i in arr1:
        a += i
    for j in arr2:
        b += j
    if len(arr1) < len(arr2):
        answer = -1
    if len(arr1) > len(arr2):
        answer = 1
    if len(arr1) == len(arr2) and a > b:
        answer = 1
    if len(arr1) == len(arr2) and a < b:
        answer = -1
    if len(arr1) == len(arr2) and a == b :
        answer = 0
        
    print(a, b)
    return answer