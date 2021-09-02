# 1. 타자게임 프로그램을 작성하시오(함수, 클래스 사용하지 않고 작성)
# - 메뉴는 문제추가, 문제저장, 문제읽기, 타자게임, 등수리스트, 종료하기가 있다.
# - 문제추가 메뉴는 문제리스트에 문제를 추가한다.
# - 문제저장 메뉴는 문제리스트를 피클을 이용하여 저장한다.
# - 문제읽기 메뉴는 파일로 저장된 문제를 문제리스트로 가져온다.
# - 문제게임 메뉴는 타자게임을 진행하고 기록한다.
# - 등수리스트는 딕셔너리에 저장된 값을 시간값이 적은 순서로 정렬하여 출력한다.

import random,time,os,pickle
dir = os.path.dirname(__file__)

class TypingGame:

    def load_question(self):
        with open(dir+'/quiz11_q.txt','rb') as f:
            self.word = pickle.load(f)

    def add_question(self):
        add_list = input('추가하실 단어를 입력하세요 >>> ')
        with open(dir+'/quiz11_q.txt','rb') as f:
            self.word = pickle.load(f)
            self.word.append(add_list)

    def save_question(self):
        with open(dir+'/quiz11_q.txt','wb') as f:
            pickle.dump(self.word,f)

    def read_question(self):
        with open(dir+'/quiz11_q.txt','rb') as f:
            self.word = pickle.load(f)
            print(self.word)

    def run_game(self):
        start = time.time()
        for i in range(1):
            #word = ["cat","dog","fox","monkey", "mouse","panda","frog","snake","wolf"]
            answer = random.choice(self.word)
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
        self.quiz11_dict = pickle.load(f)
        f.close()

        self.quiz11_dict[name] = taken_time

        f=open(dir+'/quiz11_game.txt','wb')
        pickle.dump(self.quiz11_dict,f)
        f.close

    def Lrank(self):
        f=open(dir+'/quiz11_game.txt','rb')
        self.quiz11_dict = pickle.load(f)
        f.close()
        self.quiz11_rank = sorted(self.quiz11_dict.items(), key = lambda x:x[1])
        print(self.quiz11_rank)
        for i in range(len(self.quiz11_rank)):
            print(f'{i+1}등 : {self.quiz11_rank[i][0]:10s}  {self.quiz11_rank[i][1]}초')

    
    def menuDisplay(self):
        menu = input('1.문제추가   2.문제저장   3.문제읽기   4.타자게임   5.등수리스트   6.종료하기 \n')
        return menu

    def exe(self, menu):
        
        if menu == '1':
            word = self.add_question()
        elif menu == '2':
            self.save_question()
        elif menu == '3':
            self.read_question()
        elif menu == '4':
            self.run_game()
        elif menu == '5':
            self.Lrank()
        elif menu == '6':
            print('프로그램 종료')
        else :
            print('잘못입력하셨습니다.')

    def __init__(self):
        self.load_question()
        while True:
            self.exe(self.menuDisplay())

TypingGame()