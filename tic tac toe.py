board = [" "," "," "," "," "," "," "," "," " ]
boardLog = [0, 0, 0,
        0, 0, 0,
        0, 0, 0]

player = True #with this we'll know which player's turn it is

def tic_tac_toe ():
    print ('|' ,board[0],'|',board[1] ,'|', board[2],'|')
    print ('--------------------')
    print ('|' ,board[3],'|',board[4] ,'|', board[5],'|')
    print ('--------------------')
    print ('|' ,board[6],'|',board[7] ,'|', board[8],'|')

def move(x1,x2):
    board[x2] = x1
    boardLog[x2] = 1
    tic_tac_toe()

def even (x, x2):
    while  (x%2!=0):
        x = int(input ('enter an odd number'))
    while  (board[x2]!=' '):
        x2 = int(input ('enter an empty place'))

    #Nothing here because if we get out of the while is because it's a valid number (we're not checking numbers out of range or anything)
    move (x ,x2)      

def odd (x ,x2) :
    while  (x%2==0):
        x = int(input ('enter an even number'))
    while  (board[x2]!=' '):
        x2 = int(input ('enter an empty place'))
    #Same here
    move (x ,x2)        

def winner():
    if (boardLog[0] + boardLog[1] + boardLog[2] == 3):
      if (board[0]+board [1]+board[2]==15):
          print ('you are the winner')
          return True
    if (boardLog[0] + boardLog[3] + boardLog[6] == 3):
      if (board[0]+board [3]+board[6]==15):
          print ('you are the winner')
          return True
    if (boardLog[1] + boardLog[4] + boardLog[7] == 3):
      if (board[1]+board [4]+board[7]==15):
          print ('you are the winner')
          return True
    if (boardLog[3] + boardLog[4] + boardLog[5] == 3):
      if (board[3]+board [4]+board[5]==15):
          print ('you are the winner')
          return True
    if (boardLog[2] + boardLog[5] + boardLog[8] == 3):
      if (board[2]+board [5]+board[8]==15):
          print ('you are the winner')
          return True
    if (boardLog[6] + boardLog[7] + boardLog[8] == 3):
      if (board[6]+board [7]+board[8]==15):
          print ('you are the winner')
          return True

    else: return False

def turn(s):
    print ('its '+ s +' turn')
    x = int (input ('enter the number: '))
    x1 = int (input ('enter the places number: '))
    if s == 'a':
        even(x, x1)
    else: odd(x, x1)          

print('Tic Tac Toe')
print ('player A should enter even numbers only'+' and player B should enter odd numbers only')
print ('the player with the odd numbers start')
tic_tac_toe ()
while (True):
    if(player == True):
        turn('a')
        print('True')
        player = False
    elif(player == False):
        turn('b')
        print('False')
        player = True
    if winner(): break
    else:
        if player == 'a': player = 'b'
1
