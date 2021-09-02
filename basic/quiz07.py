# quiz 06을 pickle로

import pickle,os,json
dir = os.path.dirname(__file__)

def juso_load():
    f=open(dir+'/juso_list.json','r')
    juso_list = json.load(f)
    f.close()
    return juso_list

def juso_save(juso_list):
    f=open(dir+'/juso_list.json','w')
    json.dump(juso_list,f)
    f.close()

def juso_input(juso_list):
    name = input('이름>>>')
    tel = input('전화번호>>>')
    address = input('주소>>>')
    data = [name,tel,address]
    juso_list.append(data)
    return juso_list

def juso_print(juso_list):
    # for data in juso_list:
    #     print('이름 : {}, 전화번호 : {}, 주소 : {}\n'.format(juso_list[data][0],juso_list[data][1],juso_list[data][2]))
    print(juso_list)

juso_list = []
juso_list = juso_load()
print(juso_list)
while True:
    menu_txt = '''1.입력   2.출력   3.저장 \n'''
    menu = input(menu_txt)
    if menu == '1':
        juso_list = juso_input(juso_list)
    elif menu == '2':
        juso_print(juso_list)
    elif menu == '3':
        print('프로그램 종료!')
        juso_save(juso_list)
        break
    else :
        print('잘못입력하셨습니다.')
    
print(juso_list)