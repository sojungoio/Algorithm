def solution(num_list):
    if num_list[-1] > num_list[-2]:
        i = num_list[-1]-num_list[-2]
        num_list.append(i)
    else:
        j = num_list[-1] * 2
        num_list.append(j)
    return num_list