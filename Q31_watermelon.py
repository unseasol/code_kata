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
