'''
과일을 상자에 담아서
과일 이름, 갯수 입력받기
->몇박스 몇개 나오는지 출력, 없으면 해당품목 없음 출력
'''
'''
items={'사과':8, '배':6, '귤':20}
fruit = input('과일 이름 :')
num = input('갯수 : ')


if num.isdecimal() :
    num = int(num)
    if items.get(fruit):
        nbox = num//items[fruit]
        remainder = num % items[fruit]
        print(f'{nbox}박스 {remainder}개입니다.')
    else :
        print("해당품목이 없습니다.")
else : 
    print("숫자로만 입력해주세요")
'''

'''
거스름돈 계산하기
물건값, 대금, 거스름돈 계산 지불
'''

Price = 150000
money = int(input("받은 금액 :"))
change = Price-money

if change != 0 :
    a = change//10000
    change = change - 10000*a
    b = change//5000
    change = change - 5000*b
    c = change//1000
    change = change - 1000*c
    d = change//500
    change = change - 500*d
    e = change//100
    change = change - 100*e
    f = change//50
    change = change - 50*f
    g = change//10
    change = change - 10*g

print(f'거스름돈 10000원 {a}장, 5000원 {b}장, 1000원 {c}장, 500원 {d}개, 100원 {e}개, 50원 {f}개, 10원 {g}개')