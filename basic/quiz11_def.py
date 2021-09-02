# 1. 타자게임 프로그램을 작성하시오(함수, 클래스 사용하지 않고 작성)
# - 메뉴는 문제추가, 문제저장, 문제읽기, 타자게임, 등수리스트, 종료하기가 있다.
# - 문제추가 메뉴는 문제리스트에 문제를 추가한다.
# - 문제저장 메뉴는 문제리스트를 피클을 이용하여 저장한다.
# - 문제읽기 메뉴는 파일로 저장된 문제를 문제리스트로 가져온다.
# - 문제게임 메뉴는 타자게임을 진행하고 기록한다.
# - 등수리스트는 딕셔너리에 저장된 값을 시간값이 적은 순서로 정렬하여 출력한다.

import random,time,os,pickle
dir = os.path.dirname(__file__)

def load_question():
    f=open(dir+'/quiz11_q.txt','rb')
    word = pickle.load(f)
    f.close()
    return word

def add_question():
    add_list = input('추가하실 단어를 입력하세요 >>> ')
    f=open(dir+'/quiz11_q.txt','rb')
    word = pickle.load(f)
    word.append(add_list)
    f.close()
    return word

def save_question(word):
    f=open(dir+'/quiz11_q.txt','wb')
    pickle.dump(word,f)
    f.close()

def read_question(word):
    f=open(dir+'/quiz11_q.txt','rb')
    word = pickle.load(f)
    print(word)
    f.close()

def run_game(word):
    start = time.time()
    for i in range(1):
        #word = ["cat","dog","fox","monkey", "mouse","panda","frog","snake","wolf"]
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

    print(f'총 {taken_time}초 걸렸습니다.')

    f=open(dir+'/quiz11_game.txt','rb')
    quiz11_dict = pickle.load(f)
    f.close()

    quiz11_dict[name] = taken_time

    f=open(dir+'/quiz11_game.txt','wb')
    pickle.dump(quiz11_dict,f)
    f.close

def Lrank():
    f=open(dir+'/quiz11_game.txt','rb')
    quiz11_dict = pickle.load(f)
    f.close()
    quiz11_rank = sorted(quiz11_dict.items(), key = lambda x:x[1])
    print(quiz11_rank)
    for i in range(len(quiz11_rank)):
        print(f'{i+1}등 : {quiz11_rank[i][0]:10s}  {quiz11_rank[i][1]}초')

word = load_question()

while True:
    menu = input('1.문제추가   2.문제저장   3.문제읽기   4.타자게임   5.등수리스트   6.종료하기 \n')
    if menu == '1':
        add_question()
    elif menu == '2':
        save_question(word)
    elif menu == '3':
        read_question(word)
    elif menu == '4':
        run_game(word)
    elif menu == '5':
        Lrank()
    elif menu == '6':
        print('프로그램 종료')
        break
    else :
        print('잘못입력하셨습니다.')
