# 이름, 전화번호, 주소를 입력받아서
# TXT파일에 1건당 한줄씩 저장하는 함수를 작성한다.
# 저장된 내용을 화면에 출력하는 함수를 작성한다.




def juso_input():
    name = input('이름 : ')
    tell = input('번호 : ')
    addr = input('주소 : ')
    f=open('./basic/test01.txt','a',encoding='utf8')
    f.write(f'이름 : {name}\n번호 : {tell}\n주소 : {addr}\n\n')
    f.close()

def juso_input2():
    name = input('이름 : ')
    tell = input('번호 : ')
    addr = input('주소 : ')
    f=open('./basic/test01.txt','a',encoding='utf8')
    f.write(name+','+tell+','+addr+'\n')
    f.close()

def juso_print():
    f=open('./basic/test01.txt','r',encoding='utf8')
    line=1
    while line:
        line = f.readline()
        print(line, end='')
    f.close()

def juso_print2():
    f=open('./basic/test01.txt','r',encoding='utf8')
    for line in f.readlines():
        line = line.replace('\n','')
        data = line.split(',')
        print('이름 : {}, 전화번호 : {}, 주소 : {}'.format(data[0],data[1],data[2]))
    f.close()

juso_input2()
juso_print2()