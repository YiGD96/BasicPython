# 은행 계좌를 클래스로 작성하시오
# 클래스 변수를 이용하여 계좌가 개설된 건수를 체크하고 출력하는 클래스 함수를 작성합니다.
# 아래의 내용은 인스턴스 함수와 변수로 작성합니다.
# 계좌는 이름과 금액을 입력받고, 계좌번호는 자동으로 생성합니다.
# 입금은 0보다 큰금액을 입력해야하며 로그에 입금내역을 기록합니다.
# 입금 횟수에 따라 1%의 이자가 지급됩니다.(5회마다)
# 출금은 잔액보다 작을경우에 처리됩니다. 로그에 출금 기록을 남깁니다.
# 계좌정보를 출력하는 함수는 은행이름, 예금주, 계좌번호, 잔고를 출력합니다.
# 입금내역과 출금내역을 출력하는 함수

class Account:
    # class 변수 계좌 개설 건수 
    account_count = 0

    @classmethod
    def get_account_num(cls):
        print('계좌수:',cls.account_count) 
    
    # @staticmethod
    # def get_account_num1():
    #     print('계좌수:',Account.account_count)

    def __init__(self, name, balance):
        Account.account_count += 1
        self.deposit_count = 0 # 입금횟수
        self.total_log =[]  
        self.name = name
        self.balance = balance
        self.bank = "부산은행"
        self.account_number=str(Account.account_count)

    def __str__(self):
        return "예금주: "+ self.name +" 계좌번호: "+self.account_number+" 잔고: "+str(self.balance)
    
    def display_info(self):
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)
    
    def deposit(self, amount):
        if amount >= 1:
            self.total_log.append(('입금',amount))
            self.balance += amount
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:    # 이자지급 5번마다    
                interest = int(self.balance * 0.01)
                self.balance = self.balance + interest
                self.total_log.append(('이자지급',interest))
                print(interest,'원의 이자가 지급되었습니다.')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.total_log.append(('출금',amount))
            self.balance -= amount
        else:
            print('잔액이 부족합니다.')

a = Account('hong',2000)
print(a)
a.deposit(2000)
a.deposit(100)
a.deposit(900)
a.withdraw(3000)
a.deposit(7000)
a.deposit(490)
print(a.total_log)

# 1. 계좌개설  2. 입금  3. 출금  4. 입출금내역  5. 총계좌수출력  6. 종료

account_list = []
while True:
    menu = input('1. 계좌개설  2. 입금  3. 출금  4. 입출금내역  5. 총계좌수출력  6. 종료 \n' )
    if menu == '1':
        name = input('이름 >>> ')
        a = Account(name, 0)
        account_list.append(a)
        print(a, '로 계좌가 개설되었습니다.')
    elif menu == '2':
        account_num = input('계좌번호를 입력하세요 >>> ')
        check = 0
        for acc in account_list:
            if acc.account_number == account_num:
                check =1 
                amount=int(input('입금할 금액을 입력하세요 >>> '))
                acc.deposit(amount)
                print(amount,'원이 입금되었습니다.')
            if check==0:
                print('계좌번호가 없습니다.')
    elif menu == '3':
        account_num = input('계좌번호를 입력하세요 >>> ')
        check = 0
        for acc in account_list:
            if acc.account_number == account_num:
                check =1 
                amount=int(input('출금할 금액을 입력하세요 >>> '))
                acc.withdraw(amount)
                print(amount,'원이 출금되었습니다.')
            if check==0:
                print('계좌번호가 없습니다.')
    elif menu == '4':
        account_num = input('계좌번호를 입력하세요 >>> ')
        check = 0
        for acc in account_list:
            if acc.account_number == account_num:
                check=1
                for data in acc.total_log:
                    print(data[0],data[1])
            if check ==0:
                print('계좌번호가 없습니다.')
    elif menu == '5':
        Account.get_account_num()
    elif menu == '6':
        print('프로그램 종료!')
        break
    else : 
        print('잘못된 메뉴선택')
