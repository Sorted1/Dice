import random, os
from pystyle import *
import ctypes

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

def Clear():
    os.system("cls")
ctypes.windll.kernel32.SetConsoleTitleW(f'[Dice By Sorted]')
text = """
                                            ██████╗ ██╗ ██████╗███████╗
                                            ██╔══██╗██║██╔════╝██╔════╝
                                            ██║  ██║██║██║     █████╗  
                                            ██║  ██║██║██║     ██╔══╝  
                                            ██████╔╝██║╚██████╗███████╗
                                            ╚═════╝ ╚═╝ ╚═════╝╚══════╝   """

choices = """
                                            ██████╗ ██╗ ██████╗███████╗
                                            ██╔══██╗██║██╔════╝██╔════╝
                                            ██║  ██║██║██║     █████╗  
                                            ██║  ██║██║██║     ██╔══╝  
                                            ██████╔╝██║╚██████╗███████╗
                                            ╚═════╝ ╚═╝ ╚═════╝╚══════╝                 
                                              [1] 1 Dice [2] 2 Dice"""
Clear()
print(Colorate.Horizontal(Colors.red_to_purple, choices, 1))
print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
ss324 = input("Choice: ")
Clear()
if ss324 == "1":
    print(Colorate.Horizontal(Colors.red_to_purple, text, 1))
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(f"                                                  Dice Roll: {dice1}")

if ss324 == "2":
    print(Colorate.Horizontal(Colors.red_to_purple, text, 1))
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(f"                                                  Dice Roll: {dice1}")
    print(f"                                                  Dice Roll: {dice2}")
    print(f"                                                  Total:", dice1 + dice2)
