import re,sys

class Customer:
    custlist=[{'name': '홍길동', 'gender': 'M', 'email': 'hong1@gmail.com', 'birthday': '2000'},
          {'name': '박나리', 'gender': 'F', 'email': 'park1@gmail.com', 'birthday': '1999'},
          {'name': '이지은', 'gender': 'F', 'email': 'lee01@gmail.com', 'birthday': '1988'},
          {'name': '김은희', 'gender': 'F', 'email': 'kim01@gmail.com', 'birthday': '2001'}  ]
    page=3

    def insertData(self):
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
            for i in Customer.custlist:                 # 여기서만 저장하고싶을때는 self, 모두 다에 적용 시키고 싶을 때 customer
                if i['email'] == customer['email']:
                    check = 1
            if check == 0:
                break
            print('중복되는 이메일입니다.')

        while True:
            customer['birthday'] = input('출생년도 4자리 >>> ')
            if len(customer['birthday']) == 4 and customer['birthday'].isdigit():
                break
            
        Customer.custlist.append(customer)
        page = len(Customer.custlist)-1
        print(customer)
        print(Customer.custlist)
        print(Customer.page)

    def curSearch(self):
        if Customer.page>=0:
            print(f'현재페이지는 {Customer.page+1}쪽입니다.')
            print(Customer.custlist[Customer.page])
        else:
            print('입력된 데이터가 없습니다.')

    def preSearch(self):
        if Customer.page <= 0:
            print('첫번째 페이지 입니다.')
            print(Customer.page)
        else:
            Customer.page -= 1
            print(f'현재 페이지는 {Customer.page+1}쪽입니다.')
            print(Customer.custlist[Customer.page])

    def nextSearch(self):
        if Customer.page >= len(Customer.custlist)-1:
            print('마지막 페이지입니다.')
            print('page')
        else :
            Customer.page += 1
            print(f'현재 페이지는 {Customer.page+1}쪽입니다.')
            print(Customer.custlist[Customer.page])
        
    def updateData(self):
        while True:
            choice1 = input('이메일을 입력하세요. >>> ')
            idx =-1
            for i in range(len(Customer.custlist)):
                if Customer.custlist[i]['email']==choice1:
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
                Customer.custlist[idx][choice2] = input(f'수정할 {choice2}를 입력하세요 >>> ')
                break
            elif choice2 == 'exit':
                break
            else :
                print('존재하지 않는 항목입니다.')
                break

    def deleteData(self):
        choice1 = input('삭제하려는 고객정보의 이메일을 입력하세요 >>> ')
        delok = 0
        for i in range(len(Customer.custlist)):
            if Customer.custlist[i]['email'] == choice1:
                print(f'{Customer.custlist[i]["name"]}님의 정보가 삭제되었습니다.')
                del Customer.custlist[i]
                delok = 1
                break
        if delok == 0:
            print('등록되지 않은 이메일입니다.')
        print(Customer.custlist)

    def exe(self,choice):
        if choice=='I':
            self.insertData()
        elif choice=='C':
            self.curSearch()
        elif choice=='P':
            self.preSearch()
        elif choice=='N':
            self.nextSearch()
        elif choice=='U':
            self.updateData()
        elif choice=='D':
            self.deleteData()
        elif choice=='Q':
            sys.exit()

    def firstinput(self):
        choice=input('''
            다음 중에서 하실 일을 골라주세요 :
            I - 고객 정보 입력
            C - 현재 고객 정보 조회
            P - 이전 고객 정보 조회
            N - 다음 고객 정보 조회
            U - 고객 정보 수정
            D - 고객 정보 삭제
            Q - 프로그램 종료
        ''').upper() 
        return choice

    def __init__(self):
        while True:
            self.exe(self.firstinput())

Customer()