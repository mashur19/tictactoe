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

    elif (theBoard['tl']!=' ' and 
     theBoard['tc']!=' ' and 
     theBoard['tr']!=' ' and 
     theBoard['ml']!=' ' and 
     theBoard['mc']!=' ' and 
     theBoard['mr']!=' ' and 
     theBoard['bl']!=' ' and 
     theBoard['bc']!=' ' and theBoard['br']!=' '):
        return 3

    else:
        return 0

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
            
            while True:           
                print('player'+str(player)+' enter the position for X')
                c1=input().lower()
                if c1 in theBoard.keys():    
                    if theBoard[c1]==' ':
                        break
                    else:
                        print('place already occupied')
                else:
                    print("Invalid position")
            theBoard[c1]='X'
            disBoard()   
            if winCondition() == 1 or winCondition() == 3:
                break
            while True:
                print('player'+str(nextPlayer)+' enter the position for O')
                c2=input().lower()
                if c2 in theBoard.keys():
                    if theBoard[c2]==' ':
                        break
                    else:
                        print('place already occupied')
                else:
                    print("Invalid position")
            theBoard[c2]='O'
            disBoard()
            if winCondition() == 2 or winCondition() == 3:
                break
        break

    if winCondition() == 1:
        print('player'+str(player)+' wins the game')
    elif winCondition() == 2:
        print('player'+str(nextPlayer)+' wins the game')
    elif winCondition() == 3:
        print('game is a draw')        
else:
    SystemExit