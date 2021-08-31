# 회원 정보를 입력받아서 각 항목을 체크한 후 회원가입처리 한다.
# 회원 정보는 딕셔너리에 key를 회원아이디로 value를 각 회원정보를 리스트로 저장
# 회원정보는 정규표현식을 이용하여 형식에 맞도록 입력받는다.

# 함수는 따로 만들기
# 이름은 한글로 입력 한글 [ㄱ-ㅣ가-힣]
# 아이디 영어와 숫자 [A-Za-z0-9]
# 전화번호는 지역번호 2~3자리 - 번호 3~4자리 - 번호 4자리
# 주민등록번호 생년월일6자리-1자리(1~4 내국인 5~8 외국인)6자리(숫자)
# 이메일 주소 형식(아이디 소문자, 숫자 가능 첫글자는 소문자, 전체길이가 5글자 이상)

# import re

# print('회원정보를 입력하세요')

# member = {}

# name = input('이름 >>> ')
# id = input('아이디 >>> ')
# tel = input('전화번호 >>> ')
# Rnumber = input('주민등록번호 >>> ')
# email = input('이메일 >>> ')

# member[id] = [name, tel, Rnumber, email]

# p = re.compile('[ㄱ-ㅣ가-힣]+')
# if p.match(name):
#     print('hi')
# else :
#     print('nob')

import re
member = {}

def namecheck():
    name_p = re.compile('^[ㄱ-ㅣ가-힣]{2,}$')    # 여기서 ^는 저걸로 시작해라 $는 저걸로 끝내라
    name_c = 0
    while not name_c :
        name = input('이름 >>> ')
        name_c = name_p.match(name)
        print(name_c)
    return name


def idcheck():
    id_p = re.compile('[a-z][A-Za-z0-9_]{4,11}$') # 첫 글자는 숫자 안됨 
    id_c = 0
    while not id_c :
        id = input('id >>> ')
        id_c = id_p.match(id)
        print(id_c)
    return id


# 전화번호는 지역번호 2~3자리-번호 3~4자리-번호 4자리
def telcheck():
    tel_p = re.compile('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}$')
    tel_c = 0
    while not tel_c :
        tel = input('전화번호 >>> ')
        tel_c = tel_p.match(tel)
        print(tel_c)
    return tel

def jumincheck():
    jumin_p = re.compile('[0-9]{6}-[0-9]{7}$')
    jumin_c = 0
    while not jumin_c :
        jumin = input('주민번호 >>> ')
        jumin_c = jumin_p.match(jumin)
        print(jumin_c)
    return jumin

def emailcheck():
    email_p = re.compile('[a-z][a-z0-9_]{3,10}@[a-z]+[.][a-z]+')
    email_c = 0
    while not email_c :
        email = input('이메일 >>> ')
        email_c = email_p.match(email)
        print(email_c)
    return email


def signup(member):
    name = namecheck()
    id = idcheck()
    tel = telcheck()
    jumin = jumincheck()
    email = emailcheck()
    member[id] = [name,tel,jumin,email]
    return member

signup(member)
print(member)