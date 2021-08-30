# 게임을 시작할 때 사용자가 엔터 키를 입력하면 시작한다.
# 속으로 5초를 카운트하고 엔터키를 입력하여 가장 근접한 시간 맞추는 게임
# time.time() ㅣ용
# 원하는 만큼 시도하며 그중에 가장 시간차가 작은 기록을 선택해서 출력한다.
# Q,q를 입력하면 종료한다.
# 종료시 저장된 시간이 없을 경우에 대한 처리를 한다.


import time

# time_data = []
# min_num = 100
# print("계속 하시려면 enter, 그만 두시려면 q를 누르세요")

# while True:
#     start = time.time()
#     quit = input('enter or q >>> ')
#     end = time.time()
    
#     if quit == 'q' or quit == 'Q':
#         if not time_data :
#             print("값이 없습니다.")
#         break
#     else : pass

#     diff_time = end-start
#     print('걸린시간', diff_time)
#     time_data.append(diff_time)
    
#     for i in range(len(time_data)):
#         if min_num > abs(5-time_data[i]):
#             min_num = time_data[i]
            

# print(time_data)
# print(f'5초에 제일 가까운 숫자는 {min_num}입니다.')


time_diff = []
count = 0
while True :
    count += 1
    value = input(str(count)+'번째 시도 : 시작!(종료:q)')
    if value.upper() == 'Q':
        break
    start = time.time()
    input('5초 후에 엔터!!')
    end = time.time()
    diff = end-start
    time_diff.append(diff)

if not len(time_diff) == 0:
    print(time_diff)
    time_diff1 = [data - 5 for data in time_diff]
    print(time_diff1)
    result = map(abs,time_diff1)                # map : 내역하나하나 처리
    print(result)
    result = list(result)
    print(result)
    index = result.index(min(result))
    print('실제시간 :', time_diff[index])
    print('차이 :', result[index])

else : 
    print('저장된 정보가 없습니다.')
print('프로그램 종료!!')