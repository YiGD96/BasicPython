import re

def insertData(custlist,page):
    customer = {'name':'','gender':'','email':'','birthday':''}
    customer['name'] = input('이름을 입력하세요 >>> ')
    while True:
        customer['gender'] = input('성별을 입력하세요(M/m, F/f) >>> ').upper()
        if customer['gender'] in ('M' ,'F'):
            break
        print('입력이 올바르지 않습니다.')

    while True:
        regex = re.compile('^[a-z][a-z0-9]{4,11}@[a-z]{2,}[.][a-z]{2,}$')
        while True:
            customer['email'] = input('이메일 >>> ')
            email_r = regex.search(customer['email'])
            if email_r:
                break
            else:
                print('@포함 정확한 이메일 주소를 입력하세요')
        check = 0
        for i in custlist:
            if i['email'] == customer['email']:
                check = 1
        if check == 0:
            break
        print('중복되는 이메일입니다.')

    while True:
        customer['birthday'] = input('출생년도 4자리 >>> ')
        if len(customer['birthday']) == 4 and customer['birthday'].isdigit():
            break
        
    custlist.append(customer)
    page = len(custlist)-1
    print(customer)
    print(custlist)
    print(page)
    return custlist,page

def curSearch(custlist,page):
    print(page)
    if page>=0:
        print(f'현재페이지는 {page+1}쪽입니다.')
        print(custlist[page])
    else:
        print('입력된 데이터가 없습니다.')

def preSearch(custlist,page):
    if page <= 0:
        print('첫번째 페이지 입니다.')
        print(page)
    else:
        page -= 1
        print(f'현재 페이지는 {page+1}쪽입니다.')
        print(custlist[page])
    return page

def nextSearch(custlist,page):
    if page >= len(custlist)-1:
        print('마지막 페이지입니다.')
        print('page')
    else :
        page += 1
        print(f'현재 페이지는 {page+1}쪽입니다.')
        print(custlist[page])
    return page
    
def updateData(custlist):
    while True:
        choice1 = input('이메일을 입력하세요. >>> ')
        idx =-1
        for i in range(len(custlist)):
            if custlist[i]['email']==choice1:
                idx = i
                break
        if idx == -1:
            print('등록되지 않은 이메일입니다.')
            break
        choice2 = input('''
            다음중 수정하실 정보를 선택하세요
            1.name      2.gender     3.birthday     4.exit
        ''')

        if choice2 in('name','gender','birthday'):
            custlist[idx][choice2] = input(f'수정할 {choice2}를 입력하세요 >>> ')
            break
        elif choice2 == 'exit':
            break
        else :
            print('존재하지 않는 항목입니다.')
            break
    return custlist

def deleteData(custlist):
    choice1 = input('삭제하려는 고객정보의 이메일을 입력하세요 >>> ')
    delok = 0
    for i in range(len(custlist)):
        if custlist[i]['email'] == choice1:
            print(f'{custlist[i]["name"]}님의 정보가 삭제되었습니다.')
            del custlist[i]
            delok = 1
            break
    if delok == 0:
        print('등록되지 않은 이메일입니다.')
    print(custlist)
    return custlist