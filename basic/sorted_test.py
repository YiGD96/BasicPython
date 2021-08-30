import random
# print(random.randint(1,6))
# print(random.sample(range(1,7),2))     # 중복하지 않은값 출력
# print(random.choice(['a','b','c','d']))


# lotto번호 추출 1~45사이의 5개 숫자를 뽑습니다. 중복하지 않고,
# sample() 사용한 경우, 사용하지 않은 경우로 뽑기

print(random.sample(range(1,46),5))

lott = []

for i in range(5):
    num = random.randint(1,46)
    lott.append(num)

print(lott)


for i in range(5):
    lotto=[0,0,0,0,0,0]
    for x in range(6):
        num=0
        while(num in lotto):            # 왜 중복이 안되는지????
            num = random.randint(1,45)
        lotto[x]=num
    print(sorted(lotto))


# 딕셔너리 정렬
target={3:'  cat ',5:'   tiger ',1:'   dog',4:'snake    '}
print(sorted(target))
print(target)

# lambda x:x[1]
result = sorted(target.items(), key=lambda x:x[1].strip())      # 한줄 처리 간단하게 하고 싶을때
print(result)

# 함수
def sort1(x):
    return x[1].strip()

result = sorted(target.items(),key=sort1)
print(result)


# 세번째 항목으로 내림차순 정렬하기
student_tuples = [('jone','A',15),('jane','B',12),('dave','B',10)]
print(sorted(student_tuples, key=lambda x:x[2], reverse = True))

def sort2(x):
    return x[2]

result=sorted(student_tuples, key=sort2, reverse=True)
print(result)