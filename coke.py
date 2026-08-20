amount=50
while amount>0:
    print("Amount due:", amount)
    coin=int(input(("Insert coin:")))
    if coin==25 or coin==10 or coin==5:
        amount-=coin
print("Change owed:", abs(amount))
