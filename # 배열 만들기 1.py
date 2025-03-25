# 배열 만들기 1
# 제출 내역
# 문제 설명
# 정수 n과 k가 주어졌을 때, 1 이상 n이하의 정수 중에서 k의 배수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 1 ≤ n ≤ 1,000,000
# 1 ≤ k ≤ min(1,000, n)
# 입출력 예
# n	k	result
# 10	3	[3, 6, 9]
# 15	5	[5, 10, 15]
# 입출력 예 설명
# 입출력 예 #1

# 1 이상 10 이하의 3의 배수는 3, 6, 9 이므로 [3, 6, 9]를 return 합니다.
# 입출력 예 #2

# 1 이상 15 이하의 5의 배수는 5, 10, 15 이므로 [5, 10, 15]를 return 합니다.

def solution(n, k):
    
    listexam = []

    for i in range(n) :
        listexam.append((i+1)*k)

    answer = list(filter(lambda x: x <= n, listexam))
    # answer = [x for x in listexam if x <= n]


    return answer

# return [i for i in range(k,n+1,k)]


print(solution(10, 3))