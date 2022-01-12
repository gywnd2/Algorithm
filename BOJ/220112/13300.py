n, k = map(int, input().split())
students = list()
rooms = list([0, 0] for _ in range(6))
count = 0
for _ in range(n):
    students.append(list(map(int, input().split())))
for student in students:
    # 성별
    # 여학생
    if student[0] == 0:
        rooms[student[1]-1][0] += 1
    # 남학생
    else:
        rooms[student[1]-1][1] += 1
# print(rooms)
for grade in rooms:
    if grade[0] % k == 0:
        count += grade[0]//k
    else:
        count += grade[0]//k+1

    if grade[1] % k == 0:
        count += grade[1]//k
    else:
        count += grade[1]//k+1
print(count)