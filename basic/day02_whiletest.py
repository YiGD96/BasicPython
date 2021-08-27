"""
import sys

menus = {'아이스아메리카노':3000}
prompt ='''
-------------------------------------------
1. 메뉴추가  2. 메뉴수정  3. 메뉴삭제  4. 메뉴목록  5. 종료
-------------------------------------------
'''
menu = {1:'메뉴추가', 2:'메뉴수정', 3:'메뉴삭제',4:'메뉴목록'}

while True :
    in1 = input(prompt)

    if in1 == '1':
        print(menu[1])
    elif in1 == '2':
        print(menu[2])
    elif in1 == '3':
        print(menu[3])
    elif in1 == '4':
        print(menu[4])
    elif in1 == '5':
        sys.exit()
    else:
        print('메뉴를 정확히 해주세요')

"""

import sys

menu = {'아이스아메리카노':3000}
prompt ='''
-------------------------------------------
1. 메뉴추가  2. 메뉴수정  3. 메뉴삭제  4. 메뉴목록  5. 종료
-------------------------------------------
'''

while True :
    in1 = input(prompt)

    if in1 == '1':
        price = input('가격 >>>')
        in2 = input('추가할 메뉴 입력>>>')
        if menu.get(in2):
            print('입력된 메뉴입니다.')
            print(f'{in2}메뉴 가격{price}원으로 입력처리')
        else:
            menu[in2]=price

    elif in1 == '2':
        print(menu[2])
    elif in1 == '3':
        print(menu[3])
    elif in1 == '4':
        print(menu[4])
    elif in1 == '5':
        sys.exit()
    else:
        print('메뉴를 정확히 해주세요')
