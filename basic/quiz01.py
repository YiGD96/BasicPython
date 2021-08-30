#사칙계산기 (+,-,*,/)     입력 예 : 1 + 2
# 식을 입력받아서 계산을 반복 수행, 공백이 입력되면 종료

while True:
    form = input("식을 입력해주세요 >>> ")
    if not form == '':
        quiz = form.split()
        if len(quiz) == 3:
            x=int(quiz[0])
            y=int(quiz[2])
            if quiz[1]=='+':
                print(x+y)
            elif quiz[1]=='-':
                print(x-y)
            elif quiz[1]=='*':
                print(x*y)
            elif quiz[1]=='/':
                print(x/y)
        else : 
            print('입력이 바르지 않습니다.')

    else :
        print('프로그램 종료')
        break

# eval() -> 문자열을 실행 할 때
eval("print('3333')")

user_input = input('계산식 입력 >>> ')
print(eval(user_input))