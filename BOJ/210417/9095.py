import sys
t=int(sys.stdin.readline())
testCase=[int(sys.stdin.readline()) for _ in range(t)]
solution=[0 for _ in range(max(testCase)+1)]
solution[1]=1; solution[2]=2; solution[3]=4
for i in range(4, len(solution)):
    solution[i]=solution[i-1]+solution[i-2]+solution[i-3]
for num in testCase:
    print(solution[num])