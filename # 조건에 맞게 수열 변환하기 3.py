# 조건에 맞게 수열 변환하기 3
# 제출 내역
# 문제 설명
# 정수 배열 arr와 자연수 k가 주어집니다.

# 만약 k가 홀수라면 arr의 모든 원소에 k를 곱하고, k가 짝수라면 arr의 모든 원소에 k를 더합니다.

# 이러한 변환을 마친 후의 arr를 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 1 ≤ arr의 길이 ≤ 1,000,000
# 1 ≤ arr의 원소의 값 ≤ 100
# 1 ≤ k ≤ 100
# 입출력 예
# arr	k	result
# [1, 2, 3, 100, 99, 98]	3	[3, 6, 9, 300, 297, 294]
# [1, 2, 3, 100, 99, 98]	2	[3, 4, 5, 102, 101, 100]
# 입출력 예 설명
# 입출력 예 #1

# 주어진 k인 3은 홀수이므로, 전체 배열에 3을 곱합니다. 따라서 [3, 6, 9, 300, 297, 294]을 return 합니다.
# 입출력 예 #2

# 주어진 k인 2는 짝수이므로, 전체 배열에 2를 더합니다. 따라서 [3, 4, 5, 102, 101, 100]을 return 합니다.

#1
def solution(arr, k):
    answer = []
    
    for x in arr :
        if k%2 == 1 :
            answer.append(x*k)
        else :
            answer.append(x+k)
        
    return print(answer)

#2
def solution(arr, k):
    
    return [i*k if k%2 !=0 else i+k for i in arr]


#3
def solution(arr, k):

    if k % 2 != 0:
        return list(map(lambda x: x*k , arr))
    
    return list(map(lambda x: x+k, arr))
        


