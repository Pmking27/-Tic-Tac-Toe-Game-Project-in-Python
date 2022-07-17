from art import *

def sum(a,b,c):
    return a + b + c

def list_sum(xState,zState):
    xsum = 0
    zsum = 0
    for i in xState:
        xsum += i
    for j in zState:
        zsum += j
    if xsum == 5:
        return -1
    if zsum == 5:
        return -1

    return 1    

def printBoard(xState, zState):
    zero  = 'X' if xState[0] else('O' if zState[0] else 0)
    one   = 'X' if xState[1] else('O' if zState[1] else 1)
    two   = 'X' if xState[2] else('O' if zState[2] else 2)
    three = 'X' if xState[3] else('O' if zState[3] else 3)
    four  = 'X' if xState[4] else('O' if zState[4] else 4)
    five  = 'X' if xState[5] else('O' if zState[5] else 5)
    six   = 'X' if xState[6] else('O' if zState[6] else 6)
    seven = 'X' if xState[7] else('O' if zState[7] else 7)
    eight = 'X' if xState[8] else('O' if zState[8] else 8)
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")

def checkWin(xState,zState):
    game_draw = list_sum(xState,zState)
    if game_draw == 1:
        wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        
        for win in wins:
            if(sum(xState[win[0]],xState[win[1]],xState[win[2]])==3):
                printBoard(xState,zState)
                print(x_win)
                return 1
            if(sum(zState[win[0]],zState[win[1]],zState[win[2]])==3):    
                printBoard(xState,zState)
                print(o_win)
                return 0
        return -1
    else:
        printBoard(xState,zState)
        print(game_draw_logo)            

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for X & 0 for O.
    print(welcome_logo)
    while True:
        printBoard(xState,zState)
        if turn == 1:
            print("X's Chace")
            try:
                value = int(input("Please, enter the value : "))
            except ValueError:
                print("Please Enter the Number as Value.")    
            else:    
                if xState[value] != 1:
                    if zState[value] != 1:
                        xState[value] = 1
                        turn = 0 
                    else:
                        print("O's already choose this Value, please choose different Value")     
                else:
                    print("You already choose this Value,Please choose different Value.")    
            
        else:
            print("O's Chace")
            try:
                value = int(input("Please, enter the value : "))
            except ValueError:
                print("Please Enter the Number as Value.")  
            else:    
                if zState[value] != 1:
                    if xState[value] != 1:
                        zState[value] = 1
                        turn = 1
                    else:
                        print("X's already choose this Value, please choose different Value")     
                else:
                    print("You already choose this Value,Please choose different Value.")    

        cWin=checkWin(xState,zState)
        if cWin != -1:
            break
