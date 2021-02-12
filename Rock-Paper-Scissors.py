# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:20:48 2020
@author: ruben
"""

from random import randrange

options = ["rock", "paper", "scissors"]
moves = {"rock":0, "paper":1, "scissors":2}
keepPlaying = 0

def Play(counter):
    selection = (str(input("Write rock, paper or scissors\n"))).lower()
    
    if (options.count(selection) == 1):
        iapick = randrange(3)
        
        if (moves[selection] == iapick): print("\nIt´s a draw.")
        elif (moves[selection] != 0):
            if (moves[selection] - iapick == 1): print("\nYou won.")
            else: print("\nYou lost.")
        elif (iapick == 2): print("\nYou won.")
        else: print("\nYou lost.")
        
        print("The Bot choose", options[iapick])
        repeat = input("¿Want to keep playing against the Bot?\n").lower()
        
        if (repeat == "yes") : counter = 0
        else: counter = 1
        
        return(counter)
    
    else:
        print("Isn´t valid.")
        counter = 0
        return(counter)

while (keepPlaying == 0): 
    keepPlaying = Play(0)
    print("\n")