import random

input = input("r for rock,s for scissor or p for paper:")
computer = (random.choice("rsp"))

if computer == ("r"):
    print("computer choosed rock")
if computer == ("s"):
    print("computer choosed scissors")
if computer == ("p"):
    print("computer choosed paper")

if computer == input:
    print("draw!")
if computer == ("r") and input == ("p"):
    print("you win!")
if computer == ("s") and input == ("r"):
    print("you win!")
if computer == ("p") and input == ("s"):
    print("you win!")
if computer == ("p") and input == ("r"):
    print("you lose!")
if computer == ("s") and input == ("p"):
    print("you lose!")
if computer == ("r") and input == ("s"):
    print("you lose!")
