import random
import array
roll = array.array('i', [0])
n = int(input("Enter Number of Dice: "))
t = int(input("Enter Number of Sides: "))
x = 0
for i in range(1,t):
    roll.append(0)
    def Dicerolls(n):
        for i in range(0,n):
            x = random.randrange(1,t+1,1)
            if random.randrange(1,11,1) <= 2:
                x = 1
            roll[x-1] = roll[x-1]+1

Dicerolls(n)
for i in range(0,t):
    print(str(i+1) + ": " + str(roll[i]) + "/" + str(n) + " = " + str((roll[i]/n)*100) + "%")
