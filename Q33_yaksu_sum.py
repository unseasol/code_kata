def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        length = []
        for j in range(1,i+1):
            if i % j == 0:
                length.append(j)   
                
        if len(length) % 2 == 0:
            answer += i
        elif len(length) % 2 == 1:
            answer -= i
    return answer

print(solution(13,17))