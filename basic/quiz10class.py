# 은행 계좌를 클래스로 작성하시오
# 클래스 변수를 이용하여 계좌가 개설된 건수를 체크하고 출력하는 클래스 함수를 작성합니다.
# 아래의 내용은 인스턴스 함수와 변수로 작성합니다.
# 계좌는 이름과 금액을 입력받고, 계좌번호는 자동으로 생성합니다.
# 입금은 0보다 큰금액을 입력해야하며 로그에 입금내역을 기록합니다.
# 입금 횟수에 따라 1%의 이자가 지급됩니다.(5회마다)
# 출금은 잔액보다 작을경우에 처리됩니다. 로그에 출금 기록을 남깁니다.
# 계좌정보를 출력하는 함수는 은행이름, 예금주, 계좌번호, 잔고를 출력합니다.
# 입금내역과 출금내역을 출력하는 함수


# 1. 계좌개설  2. 입금  3. 출금  4. 입출금내역  5. 총계좌수출력  6. 종료
import quiz10 as qz


account_list = []
while True:
    menu = input('1. 계좌개설  2. 입금  3. 출금  4. 입출금내역  5. 총계좌수출력  6. 종료 \n' )
    if menu == '1':
        name = input('이름 >>> ')
        a = qz.Account(name, 0)
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
        qz.Account.get_account_num()
    elif menu == '6':
        print('프로그램 종료!')
        break
    else : 
        print('잘못된 메뉴선택')
