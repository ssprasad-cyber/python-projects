# -*- coding: utf-8 -*-
"""
**project : rock - paper - scissor game using python.**

"""


import random as rd
import pyfiglet as pf

c_mind = ["Rock","Paper","Scissor"]
U_score = 0
C_score = 0
title = pf.figlet_format("ROCK - PAPER - SCISSOR",font="ansi_shadow",width = 180)
print("---------------------------------"*5,"\n")
print(title)
print("---------------------------------"*5,"\n")
print("ENTER YOUR MOVE")
print("1 ROCK \n2 PAPER \n3 ✂SCISSOR \n")
while True:
  c_inp = rd.randint(0,2)
  inp = input("enter end/END to end game\n")
  if inp.lower() == "end" :
    break
  inp = int(inp)
  if inp < 1 or inp > 3:
    print("incorrect input play again")
  if inp > 0 and inp < 4:
    if inp == c_inp+1:
      print("its a draw",f"computer: {c_mind[c_inp]} you: {c_mind[inp-1]}")
    elif inp == c_inp or (inp == 3 and c_inp == 0) :
      C_score+=1
    else:
      U_score+=1
    print(f"YOU: {c_mind[inp-1]}\t COMPUTER: {c_mind[c_inp]}\nYOUR SCORE :{U_score}\tCOMPUTER SCORE: {C_score}")
    print("\n enter AGAIN\t1 ROCK 2 PAPER 3 ✂SCISSOR \n")