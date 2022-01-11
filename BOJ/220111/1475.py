n = int(input())
sixnine=0
numbers=[0 for _ in range(10)]
for digit in str(n):
    if int(digit)==6 or int(digit)==9:
        sixnine+=1
    else:
        numbers[int(digit)]+=1

if sixnine%2==0:
    print(max(sixnine//2, max(numbers)))
else:
    print(max(sixnine//2+1, max(numbers)))

# 전체 세트의 개수 구하기
# numbers = [0 for _ in range(10)]
# sets = list()
# for digit in str(n):
#     card = numbers[int(digit)]
#     if(int(digit) != 6 and int(digit) != 9):
#         if(card != 1):
#             numbers[int(digit)] = 1
#         else:
#             sets.append(numbers)
#             numbers = [0 for _ in range(10)]
#             numbers[int(digit)] = 1
#     else:
#         if(card != 1):
#             numbers[int(digit)] = 1
#         else:
#             if(int(digit) == 6):
#                 if(numbers[9] != 1):
#                     numbers[9] = 1
#                 else:
#                     sets.append(numbers)
#                     numbers = [0 for _ in range(10)]
#                     numbers[int(digit)] = 1
#             else:
#                 if(numbers[6] != 1):
#                     numbers[6] = 1
#                 else:
#                     sets.append(numbers)
#                     numbers = [0 for _ in range(10)]
#                     numbers[int(digit)] = 1
# if sum(numbers)!=0:
#     sets.append(numbers)
# print(len(sets))