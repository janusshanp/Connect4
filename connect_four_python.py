#prompt the user to how many rows and columns you can have
n = int(input('Please choose size of gameboard: '))
board = []
count = 0

for i in range (0,n):
    board.append([])
    # print('first',board)
    for j in range (0,n):
        board[i].append(' ')
        # print('second',board)

def printboard(board):
    for list in board:
        for value in list:
            print(value +'|',end='')
        print('\n'+'-+'*n)

def turncheck(count):
    if (count%2 == 0):
        sym = 'X'
        Player= P1
    else:
        sym = 'O'
        Player = P2
    return (sym, Player)

def placecoin(board,n,inp1):
        while n > 0:
            if n == 0:
                #print('third executed')
                return False
                break
            # n is the number of columns and rows,this function will let us reiterate over each line to indicate where the coin will have to go
            #first if statement checks if there is a symbol in the bottom quadrant of the column indicated
            #if there is one it continues the while loop until n is zero
            #second if statement checks if the column seleceted is empty, if empty it reutnrs the quadrant value the coin will go to
            elif board[(n-1)][inp1] == 'X' or board[(n-1)][inp1] == 'O':
                #print('first executed')
                n = n-1
                continue
            elif board[(n-1)][inp1]==' ':
                #print('second executed')
                col1=(n-1)
                row1=(inp1)
                return(col1,row1)

#index1 is to find the rows that the symbol is in
#index2 is to find the column that the symbol is in , index 2 resets its counter to 0 after going through each list
#idk class programming yet so ive just included and statements so that they cant be negative indexes
#try and except for numbers outside the board, since theyll just be an exception
def winner(board,sym):
    index1 = 0
    for i in board:
        index2=0
        for j in i:
            if j == sym:
                try:
                    if board[index1][index2] == sym and board[index1][index2+1] == sym and board[index1][index2+2] == sym and board[index1][index2+3] == sym:
                        # print('First')
                        return True
                        break
                    if board[index1][index2] == sym and board[index1][index2-1] == sym and board[index1][index2-2] == sym and board[index1][index2-3] == sym and (index2-1) > 0 and (index2-2) > 0 and (index2-3) > 0:
                        # print(index1)
                        # print(index2)
                        # print('Second')
                        # print(board[5][-1])
                        return True
                        break
                    if board[index1][index2] == sym and board[index1+1][index2] == sym and board[index1+2][index2] == sym and board[index1+3][index2] == sym:
                        # print('Third')
                        return True
                        break
                    if board[index1][index2] == sym and board[index1-1][index2] == sym and board[index1-2][index2] == sym and board[index1-3][index2] == sym and (index1-1) > 0 and (index1-2) > 0 and (index1-3) > 0:
                        # print('Fourth')
                        return True
                        break
                    if board[index1][index2] == sym and board[index1+1][index2+1] == sym and board[index1+2][index2+2] == sym and board[index1+3][index2+3] == sym:
                        # print('Fifth')
                        return True
                        break
                    if board[index1][index2] == sym and board[index1-1][index2-1] == sym and board[index1-2][index2-2] == sym and board[index1-3][index2-3] == sym and (index1-1) > 0 and (index1-2) > 0 and (index1-3) > 0 and (index2-1) > 0 and (index2-2) > 0 and (index2-3) > 0:
                        # print('Sixth')
                        return True
                        break
                    if board[index1][index2] == sym and board[index1-1][index2+1] == sym and board[index1-2][index2+2] == sym and board[index1-3][index2+3] == sym and (index1-1) > 0 and (index1-2) > 0 and (index1-3):
                        # print('Seventh')
                        return True
                        break
                    if board[index1][index2] == sym and board[index1+1][index2-1] == sym and board[index1+2][index2-2] == sym and board[index1+3][index2-3] == sym and (index2-1) > 0 and (index2-2) > 0 and (index2-3):
                        # print('Eigth')
                        return True
                        break
                except:
                    continue
                # print(index1)
                # print(index2)
            index2 = index2 + 1
        index1 = index1 + 1
        #    return True

P1= input("Please enter name of Player 1: ")
P2= input("Please enter name of Player 2: ")

while count < (n*n):
    sym, Player = turncheck(count)
    try:
        inp = input('Enter Column: ')
        inp1 = int(inp)
    except:
        print('Invalid input, please try again!')
        continue
    if placecoin(board,n,inp1) is False:
            print("Invalid Input, please try again!")
            continue
    try:
        col1,row1= placecoin(board,n,inp1)
    except:
        print('Invalid Input, please try again!')
        continue
    board[col1][row1]=sym
    printboard(board)
    if winner(board,sym) is True:
        print(Player,'is the winner!')
        break
    count = count + 1

if count == (n*n):
    print('Tie Game, try again!')
#
