exp=list(input() for _ in range(3))
if exp[1]=="+":
    print(int(exp[0])+int(exp[2]))
else:
    print(int(exp[0])*int(exp[2]))