# 할부개월수와 상품대금을 입력받아 할부대금을 계산하는 프로그램
# 할부개월수는 3~12개월까지 가능

def installment(price, n, rate) :
    if n<3 or n>12:
        print('할부 개월수는 3개월 이상 12개월 이하까지 가능합니다.')
        installment(price, n, rate)
    else :
        pay = price*(1+rate)**n
    print('%0.1f' % pay)

installment(10000,5,0.1)
print("="*20)
# 과목명과 성적을 입력받아 총점과 평균(소수2자리)을 구하는 함수를 작성
# 예 : score(국어 = 90,영어 = 56,수학 = 34)

# 방법1
def TScore(**args):
    sum = 0
    score = list(args.values())
    for i in range(len(score)):
        sum += score[i]
    print('총 점 : ', sum)    
    print('평균 : ', sum/len(score))
TScore(국어=90,수학=80,영어=70,사회=85)

# 방법2
def score(**data):
    total=0
    count=len(data)
    for k,v in data.items():
        total+=v
        print('{} : {}점'.format(k,v))
    print('총점 : {}'.format(total))
    print('평균 : {:0.2f}'.format(total/count))

score(국어=80,수학=70)
print("="*20)

# 반장선거에서 투표한 후보자 번호들을 공백을 구분자로 하여 입력하면
# 각 값들을 분리하고 분리한 값들은 숫자로 변경하여
# 각 숫자별로 같은값의 갯수를 체크하여 출력해준다.
# 함수는 아래와 같이 작성한다.
# -공백을 구분자로 하여 입력받은 후보자 번호를 분리하는 함수
candidate = ['1 ㄱ','2 ㄴ','3 ㄷ','4 ㄹ','1 ㄱ','1 ㄱ','1 ㄱ','1 ㄱ','1 ㄱ','1 ㄱ','3 ㄷ','3 ㄷ','3 ㄷ','3 ㄷ','3 ㄷ','3 ㄷ']

def str2int(slist):
    nlist = slist.split()
    nlist = list(map(int,nlist))
    return nlist

def countvotes(votes):
    n = max(set(votes))            # 중복한거 없애고 뽑힌 후보만 세려고
    result = [0 for i in range(n)] # [0,0,0] 이런식으로 채움
    for vote in votes:
        result[vote-1] += 1
    return result

def printearns(result):
    for i in range(0, len(result)):
        print("기호 : {:2}, 득표수 :{}".format(i+1, result[i]))

a=input('후보 입력 >>> ')
print(max(set(a)))

b=str2int(a)
c=countvotes(b)
printearns(c)

# -숫자로 변경된 값들의 항목별로 갯수를 카운트 하는 함수
# -결과 값을 출력하는 함수

