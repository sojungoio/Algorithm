def solution(num_list):
    answer = []
    even_num = 0
    odd_num = 0
    for i in num_list:
        if i%2 == 0:
            even_num += 1 
        else:
            odd_num += 1
    answer.append(even_num)
    answer.append(odd_num)
    return answer

"""
다른 사람풀이 

num_list 배열 안에 있는 변수를 2로 나눴을때, 
나머지가 1 아니면 0이 나오는데 .. 그걸 answer[] 배열 안에 넣어서 n%2 일때 
0이면 0번째 배열에 +1 , 1이면 1번쩨 배열에 +1 하면되는 코드!!!! 

def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer
"""