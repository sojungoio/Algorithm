# 문제, 해결, 순차적, 효율적

"""
1. 배열안에 담겨져 있는 변수들을 읽는다. 
2. n이라는 임의의 정수가 주어질때, 그 정수가 배열에 몇개가 들어있는지 확인 
3. 확인한 결과 값을 뽑아낸다.
4. 
5.
6.

* 모르는 것 : 배열안에 담겨져 있는 변수 읽는법, 몇개 들어있는지 확인하는법
* 찾아봐야할 것 : 이하동문
"""
def solution(array, n):
   #  answer = 0
   #  #answer = array.count(n)
   #  for item in array:
   # #     if n in A:
   #      if n == item:
   #          # answer = answer + 1
   #          answer += 1
            
    return len([item for item in array if n == item])
    
#     return answer
