def solution(arr, n):
    answer = []
    for i in range(0, len(arr)):
        if len(arr) % 2 != 0:
            if i % 2 == 0:
                answer.append(int(arr[i]+n))
            else:
                answer.append(arr[i])
        if len(arr) % 2 == 0:
            if i % 2 == 0:
                answer.append(arr[i])
            else:
                answer.append(int(arr[i]+n))
    return answer