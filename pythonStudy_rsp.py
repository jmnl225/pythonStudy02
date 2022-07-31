
import random

com_rsp_list = {0: '가위', 1: '바위', 2: '보'}
rsp_list = {'가위': 0, "바위": 1, "보": 2}

#전역변수(현재 파일 어디서든 사용 가능한 변수)
winCount = 0
drawCount = 0
loseCount = 0

games = int(input('몇판할지 입력 :'))

def rsp(user, userNum, com):

    #이 함수 안에서 사용하는 변수가 전역변수임을 명시
    global winCount
    global drawCount 
    global loseCount
    
    print('나 : ' + user)
    print('컴퓨터 : ' + com_rsp_list[com])
    score = com - userNum
    if userNum == com :
        #draw = '무'
        drawCount += 1
        print(game_num, '번째 판', '비김\n')
    elif 0 < score < 2 or score == -2:
        #lose = '패'
        loseCount += 1
        print(game_num, '번째 판', '컴퓨터 승리!\n')
    else :
        #win = '승'
        winCount += 1
        print(game_num, '번째 판', '당신의 승리!\n')


#숫자 입력값이 범위 밖일 경우를 확인하는 함수
def checkError(user):
    if int(user) > 3 or int(user) < 0:
        print("잘못된 값을 입력하셨습니다. 다시 입력해주세요.")
        user = input('가위(0) 바위(1) 보(2) 입력: ')
        checkError(user)
    else :
        return true


for game_num in range(1, games + 1):

    user = input('가위(0) 바위(1) 보(2) 입력: ')

    #입력값이 유효값인지 확인 (ㅜㅜ 해당 부분은 더 수정이 가능할것같은데 구조를 모두 바꿔야해서 임시로 짜집기해봤습니다.. 이부분으로 인해 코드의 가독성이 많이 떨어졌네요ㅠ)
    if checkError(user):

        #com = com_rsp_list[random.randint(0, 2)]
        #딕셔너리로 인해 com 값이 '가위', '바위', '보'로 변합니다.
        #함수 rsp에서 필요한건 int값이므로 랜덤값만 전달하도록 변경했습니다.
        com = random.randint(0, 2)

        try:
            #받은 값이 int라면 com_rsp_list에서 값을 가져옵니다.
            rsp(com_rsp_list[int(user)], int(user), com)
        except:
            #받은 값이 str이라면 그냥 입력합니다.
            #하단 코드를 진행하기 전, str값이 '가위' '바위' '보'에 해당하지 않는 에러처리 필요
            rsp(user, rsp_list[user], com)


    #전적출력
    if game_num == games :
        #print(win, draw, lose)
        print('내 전적: {}승 {}무 {}패'.format(winCount, drawCount, loseCount))
        print('컴퓨터 전적: {}승 {}무 {}패'.format(loseCount, drawCount, winCount))
        break