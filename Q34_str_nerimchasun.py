

def solution(s):
    answer = ''
    answer = sorted(s)
    answer.reverse()
    answer = "".join(answer) # Join : 문자열을 구분자 앞의 형식으로 합쳐라
    return answer