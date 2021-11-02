import random

user=input("r=rock,p=papper,s=scissors")
computer=random.choice(['r','p','s'])
if user == computer:
  print('The match is tied')
elif user=='r' and computer=='s':
  print('You win!')
elif user=='p' and computer =='r':
  print("you win!")
elif user == 's' and computer=='p':
  print("you win!")
elif computer=='r' and user=='s':
    print("you lose!")
elif computer =='p' and user =='r':
    print("you lose!")
elif computer == 's' and user=='p':
  print("you lose!")
