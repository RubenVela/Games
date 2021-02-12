# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:46:26 2021

@author: ruben

"""

from random import randrange

turn = "Bot"
repeatTurn = True
play = True
repeatGame = True
board = [[" ", " ", " "], [" "," "," "], [" "," "," "]]

def ShowBoard():
    print(board[0])
    print(board[1])
    print(board[2], "\n")        

def PlayerCoords():
    global x
    global y
    y,x = input("\bChoose where to place your mark (y x) ").split()
    x= int(x)
    y= int(y)
    return()
    
def BotCoords():
    global j
    global i
    i= randrange(3)
    j= randrange(3)
    return()
    
def PlayerMove(y,x): 
    if ((0 <= x)&(x <= 2))&((0 <= y)&(y <= 2)):
        if (board[y][x] == " "): 
            board[y][x] = "O"
            return(False)
        else: 
            print("Mark already in board")
            return(True)
    else: print("Input out of range")
    return(True)
   
def BotMove(j,i):
    if (board[j][i] == " "): 
        board[j][i] = "X"
        return(False)
    else: 
        return(True)

def CheckVictory(turn):
    global play
    if (board[0][0]==board[0][1]==board[0][2] != " "):
        print(turn, "wins")
        play = False
    elif (board[1][0]==board[1][1]==board[1][2] != " "):
        print(turn, "wins")
        play = False
    elif (board[2][0]==board[2][1]==board[2][2] != " "):
        print(turn, "wins")
        play = False
    elif (board[0][0]==board[1][0]==board[2][0] != " "):
        print(turn, "wins")
        play = False
    elif (board[0][1]==board[1][1]==board[2][1] != " "):
        print(turn, "wins")
        play = False
    elif (board[0][2]==board[1][2]==board[2][2] != " "):
        print(turn, "wins")
        play = False
    elif (board[0][0]==board[1][1]==board[2][2] != " "):
        print(turn, "wins")
        play = False
    elif (board[0][2]==board[1][1]==board[2][0] != " "):
        print(turn, "wins")
        play = False
    return()
    
while (repeatGame == True):
    turn = input("Who starts, Bot or Player? ")
    while (play == True):     
        while (repeatTurn == True):
            if (turn == "Bot"):
                BotCoords()
                repeatTurn = BotMove(j,i)    
            else:
                PlayerCoords()
                repeatTurn = PlayerMove(y,x)            
        ShowBoard()
        CheckVictory(turn)
        if (turn == "Bot"): turn = "Player"  
        else: turn = "Bot"  
        repeatTurn = True
        
    print("Game Over")
    if (input("Want to keep playing? (Y or N): ") == "N"):
        repeatGame = False 
   
    play = True
    board = [[" ", " ", " "], [" "," "," "], [" "," "," "]]