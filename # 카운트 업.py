# 카운트 업
# 제출 내역
# 문제 설명
# 정수 start_num와 end_num가 주어질 때, start_num부터 end_num까지의 숫자를 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 0 ≤ start_num ≤ end_num ≤ 50
# 입출력 예
# start_num	end_num	result
# 3	10	[3, 4, 5, 6, 7, 8, 9, 10]
# 입출력 예 설명
# 입출력 예 #1

# 3부터 10까지의 숫자들을 담은 리스트 [3, 4, 5, 6, 7, 8, 9, 10]를 return합니다.

def solution(start_num, end_num):

    # answer = []

    # for i in range(end_num+1):
    #     if i >= start_num :
    #         answer.append(i)
    #     else:
    #         continue

    # return answer

    return list(range(start_num, end_num+1))

# range() 함수는 주어진 범위의 시작 값부터 끝 값 전까지 숫자를 생성합니다. 즉, range(start_num, end_num)는 start_num에서 시작하여 end_num - 1까지의 숫자를 포함합니다. 따라서, end_num까지 포함하려면 end_num + 1을 해야 합니다.

    

print(solution(3,10))
