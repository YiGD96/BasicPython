# _game : 등수 파일
# _q : 문제목록 파일
# _def : 함수로 바꿔서 푼 문제
# _def_seperate : function을 활용한 것
# _def_function : def에서 함수만 빼 놓은것
# _class : 클래스로 바꿔서 푼 문제


# 1. 타자게임
# -문제는 문제리스트에서 5문제가 랜덤으로 출제하며, 못맞춘 문제는 맞출때까지 나오며, 문제를 맞추면 다음 문제가 출제된다.
# word = ["cat","dog","fox","monkey", "mouse","panda","frog","snake","wolf"]
# -타자 게임을 진행하고 시간을 체크하여 이름을 입력받아 딕셔너리에 key를 이름으로 value를 진행시간으로 하여 저장한다.
# rank={'hong':14.1212}
# -게임 기록은 파일로 프로그램이 실행될때 읽어오고, 종료될 때 저장한다.

import random,time,os,pickle,json
dir = os.path.dirname(__file__)


# start = time.time()
# for i in range(1):
#     #word = ["cat","dog","fox","monkey", "mouse","panda","frog","snake","wolf"]
#     answer = random.choice(word)
#     print("문제 : ",answer)
#     typing = input('답 >>> ')
#     right = 0
#     while not right:
#         if answer == typing:
#             right = 1
#             print('정답')
#         else :
#             typing = input('답 >>> ')
    
# end = time.time()

# name = input('이름 >>> ')

# taken_time = round((end-start) , 3) 

# print(f'총 {taken_time}초 걸렸습니다.')

# f=open(dir+'/quiz11_game.txt','rb')
# quiz11_dict = pickle.load(f)
# f.close()

# quiz11_dict[name] = taken_time

# f=open(dir+'/quiz11_game.txt','wb')
# pickle.dump(quiz11_dict,f)
# f.close

# print(quiz11_dict)

# 2. 타자게임 프로그램을 작성하시오(함수, 클래스 사용하지 않고 작성)
# - 메뉴는 문제추가, 문제저장, 문제읽기, 타자게임, 등수리스트, 종료하기가 있다.
# - 문제추가 메뉴는 문제리스트에 문제를 추가한다.
# - 문제저장 메뉴는 문제리스트를 피클을 이용하여 저장한다.
# - 문제읽기 메뉴는 파일로 저장된 문제를 문제리스트로 가져온다.
# - 문제게임 메뉴는 타자게임을 진행하고 기록한다.
# - 등수리스트는 딕셔너리에 저장된 값을 시간값이 적은 순서로 정렬하여 출력한다.

f=open(dir+'/quiz11_q.txt','rb')
word = pickle.load(f)
f.close()

while True:
    menu = input('1.문제추가   2.문제저장   3.문제읽기   4.타자게임   5.등수리스트   6.종료하기 \n')
    if menu == '1':
        add_list = input('추가하실 단어를 입력하세요 >>> ')
        f=open(dir+'/quiz11_q.txt','rb')
        word = pickle.load(f)
        word.append(add_list)
        f.close()
        '''
        여러개 넣고 싶을 때
        quiz =1 
        while quiz:
            quiz = input('추가할 단어 입력(종료:0) >> ')
            if quiz == '0':
                print('입력을 종료합니다.')
                break
            word.append(quiz)
        print(word)
        '''
    elif menu == '2':
        f=open(dir+'/quiz11_q.txt','wb')
        pickle.dump(word,f)
        f.close()
    elif menu == '3':
        f=open(dir+'/quiz11_q.txt','rb')
        word = pickle.load(f)
        print(word)
        f.close()
    elif menu == '4':
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
    elif menu == '5':
        f=open(dir+'/quiz11_game.txt','rb')
        quiz11_dict = pickle.load(f)
        f.close()
        quiz11_rank = sorted(quiz11_dict.items(), key = lambda x:x[1])
        print(quiz11_rank)
        
        # 이부분선생님거 다시보기
        for i in range(len(quiz11_rank)):
            print(f'{i+1}등 : {quiz11_rank[i][0]:10s}  {quiz11_rank[i][1]}초')

    elif menu == '6':
        print('프로그램 종료')
        break
    else :
        print('잘못입력하셨습니다.')
