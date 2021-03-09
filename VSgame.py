#라이브러리---------------------------------------------------
import sys # 프로그램 종료 함수 포함
import time # 시간지연 함수 포함
import random # 랜덤수 함수 포함

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
is_player_restrain = 0 #플레이어 구속 여부
is_monster_restrain = 0 #몬스터 구속 여부
turn = 0 #현재 턴 수

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
    print('\"당신은 몬스터를 마주했다.\"')
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
    global turn
    player_hp = default_player_hp
    player_atk = default_player_atk
    monster_hp = default_monster_hp
    monster_atk = default_monster_atk
    turn = 0
    print('데이터초기화 완료\n\n')

def Exit(): #3.게임종료
    print('플레이해주셔서 감사해요!')
    time.sleep(1.2) #1.2초 지연
    sys.exit() #프로그램 종료

#게임시스템-심층적#
def PlayerActSelect(): #플레이어의 턴 행동선택
    global turn
    turn += 1
    print('무엇을 할까?\t(턴:%d)'%turn)
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
    print('남은 몬스터의 HP:',monster_hp)
    #MonsterActSelect()


def PlayerActPhysicalAttack():
    print('플레이어는 상대를 배었다!')
    global monster_hp
    global player_atk
    damage = int(player_atk * 0.7)
    monster_hp -= damage
    print('몬스터는 %d의 피해를 입었다!' %damage)

def PlayerActMagicAttack():
    print('플레이어는 전격공격을 하였다!')
    global monster_hp
    global player_atk
    damage = int(player_atk * 0.5)
    monster_hp -= damage
    print('몬스터는 %d의 피해를 입었다!' %damage)

def PlayerActBind():
    print('플레이어는 구속을 시도했다. ')
    monster_restrain_percent = random.randint(0,10)
    time.sleep(1)
    if monster_restrain_percent >= 8:
        print('성공!')
        global is_monster_restrain
        is_monster_restrain = 1
    else:
        print('실패했다...')


def MonsterActSelect():
    global is_monster_restrain
    if is_monster_restrain == 1:
        print('몬스터는 움직일 수 없다!')
        return
    monster_act = random.random(1,4)
    if monster_act == 1:
        print('몬스터는 주먹을 내질렀다!')
    elif monster_act == 2:
        print('몬스터는 파이어볼을 당신에게 던졌다!')
    elif monster_act == 3:
        print('몬스터는 덩쿨을 손에 들었다.')



#메인코드-----------------------------------------------------
Mainmenu()