# 지뢰찾기(빨리찾아서 터뜨리기)
# 필드(2차원 배열 10*10)
def start_game():
    fields = list() # 저장타입 -> 양수
    for i in range(10):
        fields.append([0]*10)
    #10개의 지뢰를 임의의 위치에 저장
    import random
    nums = list(range(100))
    for i in random.sample(nums,10):
        row = i // 10 # 행 몫
        col = i % 10 # 열 나머지
        fields[row][col] = 9 # 지뢰위치
        #8방 위치 1증가
        if row < len(fields)-1:
            fields[row+1][col]+=1#남
        if row < (len(fields)-1) and col < (len(fields)-1):
            fields[row+1][col+1]+=1#남동
        if col < (len(fields)-1):
            fields[row][col+1]+=1 #동
        if row > 0 and col < (len(fields)-1):
            fields[row-1][col+1]+=1 # 북동
        if row > 0:    
            fields[row-1][col]+=1 #북
        if row > 0 and col > 0:
            fields[row-1][col-1]+=1 #북서
        if col > 0:
            fields[row][col-1]+=1 #서
        if row < (len(fields)-1) and col > 0:
            fields[row+1][col-1]+=1 #남서
    fields2 = list()
    for i in range(10):
        fields2.append(['-']*10)
    count = 10
    while(True):
        row = int(input("행좌표 입력(0~9) "))
        col = int(input("열좌표 입력(0~9) "))
        fields2[row][col] = str(fields[row][col])
        if fields[row][col]>=9:
            count-=1
            print("지뢰의 개수는 ", count)
            if count == 0:
                print("축하드립니다. 지뢰를 모두 찾으셨습니다. 게임을 종료합니다")
                break
        display(fields)
        display(fields2)
