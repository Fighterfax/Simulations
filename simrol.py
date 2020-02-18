import random


numFlips = int(input("How many flips? "))
countHeads = 0
countTails = 0
flips = [0] * numFlips
i = 0
while i < numFlips:
    
    flip = random.randint(0,1)
    if flip == 1:
        flips[i] = 1
    else:
        flips[i] = 0
    i += 1
    
print(flips)
print(countHeads)
print(countTails)
print(f"Heads = {countHeads} = {(countHeads/numFlips*100)}")
print(f"Tails = {countTails} = {(countTails/numFlips*100)}")


