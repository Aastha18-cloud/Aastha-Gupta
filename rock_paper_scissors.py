import random
print("===================")
print("Rock Paper Scissors")
print("===================")
print("1) ✊")
print("2) ✋")
print("3) ✌️")
player=int(input("Pick a number: "))
print("You chose:", player)
player2=random.randint(1,3)
print("CPU chose:", player2)
if player==1 and player2==3:
    print("You win!")
elif player==2 and player2==1:
    print("You win!")
elif player==3 and player2==2:
    print("You win!")
elif player==player2:
    print("It's a tie!")
else:
    print("CPU wins!")
