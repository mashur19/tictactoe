import random

theBoard={'tl':' ','tc':' ','tr':' ','ml':' ','mc':' ','mr':' ','bl':' ','bc':' ','br':' '}

#display board function to display board after every move 
def disBoard():   
    print('--------------------')
    print('  '+theBoard['tl'] +'  |  ' + theBoard['tc']+'  |  ' +theBoard['tr'])
    print('  '+theBoard['ml'] +'  |  ' + theBoard['mc']+'  |  ' +theBoard['mr'])          
    print('  '+theBoard['bl'] +'  |  ' + theBoard['bc']+'  |  ' +theBoard['br'])
    print('--------------------')

#check for winning condition 
def winCondition():
    if ((theBoard['tl']=='X' and theBoard['tc']=='X' and theBoard['tr']=='X') 
     or (theBoard['ml']=='X' and theBoard['mc']=='X' and theBoard['mr']=='X')
     or (theBoard['bl']=='X' and theBoard['bc']=='X' and theBoard['br']=='X')
     or (theBoard['tl']=='X' and theBoard['ml']=='X' and theBoard['bl']=='X')
     or (theBoard['tc']=='X' and theBoard['mc']=='X' and theBoard['bc']=='X')
     or (theBoard['tr']=='X' and theBoard['mr']=='X' and theBoard['br']=='X')
     or (theBoard['tl']=='X' and theBoard['mc']=='X' and theBoard['br']=='X')
     or (theBoard['tr']=='X' and theBoard['mc']=='X' and theBoard['bl']=='X')):
        return 1

    elif ((theBoard['tl']=='O' and theBoard['tc']=='O' and theBoard['tr']=='O') 
     or (theBoard['ml']=='O' and theBoard['mc']=='O' and theBoard['mr']=='O')
     or (theBoard['bl']=='O' and theBoard['bc']=='O' and theBoard['br']=='O')
     or (theBoard['tl']=='O' and theBoard['ml']=='O' and theBoard['bl']=='O')
     or (theBoard['tc']=='O' and theBoard['mc']=='O' and theBoard['bc']=='O')
     or (theBoard['tr']=='O' and theBoard['mr']=='O' and theBoard['br']=='O')
     or (theBoard['tl']=='O' and theBoard['mc']=='O' and theBoard['br']=='O')
     or (theBoard['tr']=='O' and theBoard['mc']=='O' and theBoard['bl']=='O')):
        return 2

    else:
        return 0

#def main:

#ask the player to start the game 
print(r'''Welcome to TicTacToe
--------------------
  tl  |  tc  |  tr
  ml  |  mc  |  mr            
  bl  |  bc  |  br
--------------------
DO YOU WANT TO PLAY THE GAME(Y/N)?''')

playChoice=input()

if playChoice.lower() == 'y':
    player=random.randint(1,2)
    nextPlayer= 2 if player == 1 else 1

    print('player'+str(player)+' is X'+' and player'+str(nextPlayer)+' is O')
    disBoard()
    for i in range(9):
        while winCondition() == 0:
            print('player'+str(player)+' enter the position for X')
            c1=input().lower()
            theBoard[c1]='X'
            disBoard()
            if winCondition() == 1:
                break
            print('player'+str(nextPlayer)+' enter the position for O')
            c2=input().lower()
            theBoard[c2]='O'
            disBoard()
        break

    if winCondition() == 1:
        print('player'+str(player)+' wins the game')
    else:
        print('player'+str(nextplayer)+' wins the game')    
else:
    SystemExit
'''
#capture move made by the player
def capturePos(str):
    if str.isaplha == True:
        theBoard[str]='X'
    elif str.isalpha == True:
        theBoard[str]='O'
'''


