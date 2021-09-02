#  쓰기

# f = open('./basic/test01.txt','w',encoding='utf8')
# f.write('테스트용')
# f.close()

f=open('./basic/test01.txt','r',encoding='utf8')
# print(f.readline())
# print(f.readlines())

for line in f.readlines():
    print(line, end='')
f.close()

print('\n','='*30)

f=open('./basic/test01.txt','r',encoding='utf8')
line=1
while line:
    line = f.readline()
    print(line, end='')
f.close()

print('\n','='*30)

#자동 close
with open('./basic/test01.txt','r',encoding='utf8') as f:
    line=1
    while line:
        line = f.readline()
        print(line, end='')


print('\n','='*30)


import pickle,os
# print(__file__)
dir = os.path.dirname(__file__)
# print(dir)
# f= open(dir+'/test02.txt', 'wb')      #wb, rb란??? 컴퓨터 언어(binary)로 쓴것
# data = {1:'python',2:'you need'}
# pickle.dump(data,f)                   # dump랑 dumps 차이
# f.close()

f=open(dir+'/test02.txt','rb')
result = pickle.load(f)
f.close()

print(type(result))
print(result)

print('\n', '='*30)

import json
data = [1,2,3,{'4':5, '6':7}]
result1 = json.dumps(data,separators=(',',':')) # json 문자열을 따르는 거로 바꿔줌 (다른 파일 이동시킬때)
result2 = json.dumps(data)
result3 = json.dumps(data,indent =2) # 들여쓰기해서 보여줌
print(type(result1))
print(result1)
print(type(result2))
print(result2)
print(result3)

result4 = json.loads(result1)       #loads는 읽을수 있게 바꿔줌
print(type(result4))
print(result4)