N = int(input())
route = input().split()
currLoc = [1, 1]
for command in route:
    if command == "L":
        if currLoc[1] == 1:
            continue
        else:
            currLoc[1] -= 1
    elif command == "R":
        if currLoc[1] == N:
            continue
        else:
            currLoc[1]+=1
    elif command=="U":
        if currLoc[0] == 1:
            continue
        else:
            currLoc[0]-=1
    elif command=="D":
        if currLoc[0] == N:
            continue
        else:
            currLoc[0]+=1
print(currLoc[0], currLoc[1])