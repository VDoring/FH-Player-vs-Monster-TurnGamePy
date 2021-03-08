#라이브러리---------------------------------------------------
import sys # 프로그램 종료 함수 포함
import time # 시간지연 함수 포함

#변수 및 함수-------------------------------------------------
#데이터#
default_player_hp = 1000
default_player_atk = 100
default_monster_hp = 2000
default_monster_atk = 50
player_hp = 0
player_atk = 0
monster_hp = 0
monster_atk = 0

#게임메뉴#
def Mainmenu(): #메인화면
    print('[MAIN] VS Game \\\\ Python Game Project by VDoring')
    print('메뉴를 선택해주세요.\n[1]시작\t\t[2]초기화\t[3]종료')
    user_input = int(input())
    if user_input == 1:
        ResetData()
        Gameplay()
    elif user_input == 2:
        ResetData()
        Mainmenu()
    elif user_input == 3:
        Exit()
    else:
        print('아무래도 잘못된 값이 입력된 것 같아요. 다시 메인화면으로 돌아갈께요!')
        time.sleep(0.8) #1.2초 지연
        Mainmenu()

#게임시스템-전반적#
def Gameplay(): #1.게임시작
    print('상황: 당신은 몬스터를 마주했다.')
    PlayerActSelect()

def ResetData(): #2.데이터초기화
    global player_hp
    global player_atk
    global monster_hp
    global monster_atk
    global default_player_hp
    global default_player_atk
    global default_monster_hp
    global default_monster_atk
    player_hp = default_player_hp
    player_atk = default_player_atk
    monster_hp = default_monster_hp
    monster_atk = default_monster_atk
    print('데이터초기화 완료')

def Exit(): #3.게임종료
    print('플레이해주셔서 감사해요!')
    time.sleep(1.2) #1.2초 지연
    sys.exit() #프로그램 종료

#게임시스템-심층적#
def PlayerActSelect(): #플레이어의 턴 행동선택
    print('무엇을 할까?')
    print('1.물리공격   2.마법공격   3.구속')
    user_act = int(input())
    if user_act == 1:
        PlayerActPhysicalAttack()
    elif user_act == 2:
        PlayerActMagicAttack()
    elif user_act == 3:
        PlayerActBind()
    else:
        print('다시 입력해주세요.')
        PlayerActSelect()

def PlayerActPhysicalAttack():
    print('플레이어는 상대를 배었다!')
    

def PlayerActMagicAttack():
    print('플레이어는 전격공격을 하였다.')

def PlayerActBind():
    print('플레이어는 상대를 구속하려고 하였다.')


#메인코드-----------------------------------------------------
Mainmenu()