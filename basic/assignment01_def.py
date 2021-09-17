import re,sys
import assignment01_function as cf

custlist=[{'name': '홍길동', 'gender': 'M', 'email': 'hong1@gmail.com', 'birthday': '2000'},
          {'name': '박나리', 'gender': 'F', 'email': 'park1@gmail.com', 'birthday': '1999'},
          {'name': '이지은', 'gender': 'F', 'email': 'lee01@gmail.com', 'birthday': '1988'},
          {'name': '김은희', 'gender': 'F', 'email': 'kim01@gmail.com', 'birthday': '2001'}  ]
page=3

def exe(choice,page,custlist):
    if choice=='I':
        page, custlist = cf.insertData(custlist,page)
    elif choice=='C':
        cf.curSearch(custlist,page)
    elif choice=='P':
        page = cf.preSearch(custlist,page)
    elif choice=='N':
        page = cf.nextSearch(custlist,page)
    elif choice=='U':
        custlist = cf.updateData(custlist)
    elif choice=='D':
        custlist = cf.deleteData(custlist)
    elif choice=='Q':
        sys.exit()
    return page, custlist

while True:
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
    page,custlist = exe(choice,page,custlist)

    #마지막 테스트