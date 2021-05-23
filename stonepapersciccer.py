import random

rock = ''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
computer='''
 
                     ,.
                     |`:.
                     |  `:.
               m1a   | |`.`:;@.
                     | |;.`.`;|
                     ; `.';| ||
                    ,(`;.`.| ||
                   /8o (`:.  ||
                 /o8888o  `; ||
               /@o8888888o (`;|
              (`.()oO888888o (<
               `.`.;:oO08c{)/ |
                 `.`.(),0 /  /
                   `.`.`/  /
                     `.( /
'''
n = int(input("maximum score to win       :      "))
user_score = 0
computer_score = 0
while user_score != n and computer_score != n:
    user = input(" choose:0 for rock ,1 for paper , 2 for scissor     :  ")
    if user == "0":
        print(rock)
    elif user == "1":
        print(paper)
    else:
        print(scissors)
    print("computer chose")
    cchoice =str(random.randint(0, 2))
    if cchoice == "0":
        print(rock)
    elif cchoice == "1":
        print(paper)
    else:
        print(scissors)
    if user == cchoice:
        print("draw")
    elif (user == "0" and cchoice == "2") or (user == "1" and cchoice == "0") or (user == "2" and cchoice == "1"):
        print("user won the round ")
        user_score=user_score+1
    else:
        print("comp won the round ")
        computer_score=computer_score+1

if user_score == n:
    print("---------------------------------------------------------------------------------------------------")
    print("USER WON")
if computer_score == n:
    print("---------------------------------------------------------------------------------------------------")
    print("COMPUTER WON")
    print(computer)
