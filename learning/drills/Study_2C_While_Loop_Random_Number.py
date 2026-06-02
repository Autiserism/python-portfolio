#Write a while loop that generates a random number between 1 and 10
#on each pass and prints it Stop the loop when it generates a 5.

#Option 1
import random
i=0
while i != 5:
    i=random.randint(1,10)
    print (i)

#Option2
while True:
    i = random.randint(1, 10)
    print(i)
    if i == 5:
        break
