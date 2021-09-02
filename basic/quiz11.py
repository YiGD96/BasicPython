# 1. 타자게임
# -문제는 문제리스트에서 5문제가 랜덤으로 출제하며, 못맞춘 문제는 맞출때까지 나오며, 문제를 맞추면 다음 문제가 출제된다.
# word = ["cat","dog","fox","monkey", "mouse","panda","frog","snake","wolf"]
# -타자 게임을 진행하고 시간을 체크하여 이름을 입력받아 딕셔너리에 key를 이름으로 value를 진행시간으로 하여 저장한다.
# rank={'hong':14.1212}
# -게임 기록은 파일로 프로그램이 실행될때 읽어오고, 종료될 때 저장한다.

import random,time

rank = {}

start = time.time()
for i in range(5):
    word = ["cat","dog","fox","monkey", "mouse","panda","frog","snake","wolf"]
    answer = random.choice(word)
    print("문제 : ",answer)
    typing = input('답 >>> ')
    right = 0
    while not right:
        if answer == typing:
            right = 1
            print('정답')
        else :
            typing = input('답 >>> ')
    
end = time.time()

name = input('이름 >>> ')

taken_time = round((end-start) , 3) 

rank[name] = taken_time

print(f'총 {taken_time}초 걸렸습니다.') #소수점 쓸때  : 붙어야함

print(rank)
    










# 2. 타자게임 프로그램을 작성하시오(함수, 클래스 사용하지 않고 작성)
# - 메뉴는 문제추가, 문제저장, 문제읽기, 타자게임, 등수리스트, 종료하기가 있다.
# - 문제추가 메뉴는 문제리스트에 문제를 추가한다.
# - 문제저장 메뉴는 문제리스트를 피클을 이용하여 저장한다.
# - 문제읽기 메뉴는 파일로 저장된 문제를 문제리슽느로 가져온다.
# - 문제게임 메뉴는 타자게임을 진행한다.
# - 등수리스트는 딕셔너리에 저장된 값을 시간값이 적은 순서로 정렬하여 출력한다.
# - 종료하기 메뉴는 시간기록이 저장된 딕셔너리를 저장하고 종료한다. 