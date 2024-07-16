# def solution(numbers):
#     num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#     sums = []
#     total = 0
#     for i in range(len(numbers)):
#         if numbers[i] not in num_list:
#             sums.append(numbers[i])

#     total = sum(sums)
#     return sums

def solution(numbers):
    total = 45-sum(numbers)
    return total
