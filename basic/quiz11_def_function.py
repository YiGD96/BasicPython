import random,time,os,pickle,json
dir = os.path.dirname(__file__)

def load_question():
    dir = os.path.dirname(__file__)
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
