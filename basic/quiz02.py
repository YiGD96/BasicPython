# 숫자 맞추기 (숫자 범위는 1~100)
# 컴푸터가 숫자를 정하면 맞출 때 까지
import random

num = random.randint(1,100)
count = 0

print(num)
while True: 
    count+=1
    Mynum = int(input("1~100까지의 수자를 입력해주세요 >>> "))
    if num > Mynum :
        print('숫자가 작습니다.')
    elif num < Mynum :
        print('숫자가 큽니다.')
    elif num == Mynum :
        print(f'OK 총 {count}회 실행하였습니다.')
        break
    
