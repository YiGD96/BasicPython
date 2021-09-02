# 사칙연산 맞추기 게임
# 컴퓨터가 사칙연산 문제를 랜덤으로 제출
# / -> 정수 값까지만 입력
# 5문제 제출, 몇개 맞췄는지 출력
# 걸린 시간 체크, 기록

# import random
# calculation = ['+','-','*','/']
# count = 0
# right = 0
# wrong = 0


# while True:
#     count += 1
#     a=int(random.randint(1,10))
#     b=int(random.randint(1,10))
#     oper=random.choice(calculation)
    

#     print(f'{a} {oper} {b} = ?')
#     c=int(input('정답 : '))

#     if a  b == c:               # *+-/ 어떻게 넣는지?
#         print('정답입니다.')
#         right += 1

#     else :
#         print('틀렸습니다.')
#         wrong += 1

#     if count ==5:
#         print(f'총 {right}개 맞췄습니다.')

#         break

import random, time
from operator import itemgetter

#[이름, 맞춘갯수, 걸린시간]
rank=[['aaa',4,12],['bbb',5,20]]
calculation = ['+','-','*','/']

print(sorted(rank, key=lambda x:x[1], reverse=True))    # x:x[1] {'a','b'} -> b기준으로 정렬 
print(sorted(rank, key=itemgetter(1), reverse=True))

def multisort(xs,specs):
    for key,reverse in reversed(specs):
        xs.sort(key=itemgetter(key),reverse=reverse)
    return xs

while True:
    count=0
    start = time.time()
    for i in range(5):
        a = random.randint(1,50)
        b = random.randint(1,50)
        op = random.choice(calculation)
        quiz = f'{a} {op} {b}'
        print(quiz, '=')
        print(eval(quiz))
        c = input('정답 >>> ')

        if c=='':
            c=0
        else :
            c=int(c)
        
        if int(eval(quiz)) == c:
            print('정답')
            count += 1
        else : 
            print('오답!')

    end = time.time()

    print('걸린시간 :', int(end-start))
    print('맞춘시간 :', count)
    name = input('이름입력 >>> ')
    rank.append([name,count,int(end-start)])
    print(rank)

    if 'Q' == input('종료(Q), 계속(enter)').upper() :
        break
    result = multisort(rank,((1,True),(2,False)))

    for i, item in enumerate(result):
        print(f'{i+1}등 {item}')