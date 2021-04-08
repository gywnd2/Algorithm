id_List=['kim', 'park', 'choi', 'lee', 'yoon']
pass_List=[111, 222, 333, 444, 555]
id=input("id 입력: ")

if id in id_List:
    pw = int(input("비밀번호 입력: "))
    i=id_List.index(id)
    if pw==pass_List[i]:
        print("Welcome!")
    else:
        print("비밀번호가 다릅니다!")
else:
    print("id가 없습니다!")