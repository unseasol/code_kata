# 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요.
# 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

# 제한 조건
# n은 길이 10,000이하인 자연수입니다.

# def solution(n):
#     word = "수박수박"
#     long_word = []
#     for _ in n :
#         long_word.append(word)
#     answer = long_word[:n]
#     return answer

# solution(3)

# word = "수박수박"
# word_list = []

# for i in range(3) :
#     word_list.append(word)
# print(word_list)

def solution(n):
    word = "수박수박"

    for _ in range(n):
        word += "수박수박"

    answer = word[:n]  # 단어의 특정 부분만 선택하고 싶은 경우는 문자열에서 인덱싱
    return answer
