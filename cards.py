import random
deck = []
suits = ["♠","♣","♥","♦"]
for i in range(4):
    for j in range(1,14):
        value = str(j)
        if (j == 11):
            value = "J"
        elif (j == 12):
            value = "Q"
        elif (j == 13):
            value = "K"
        elif (j == 1):
            value = "A"
        deck.append(f"{value}{suits[i]}")
        
print(deck)

for i in range(len(deck)-1, 0, -1): 

    j = random.randint(0, i + 1)  


    deck[i], deck[j] = deck[j], deck[i]  

print ("The shuffled deck is : " +  str(deck))
