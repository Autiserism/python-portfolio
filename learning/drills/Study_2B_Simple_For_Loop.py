#Write a for loop that prints numbers 1 to 20 but:
#Skips any number divisible by 3
#Stops completely if it hits a number divisible by 7
for i in range(0, 21):
    if i % 3 == 0 :
        continue
    elif i % 7 == 0 :
        break
    print(i)
