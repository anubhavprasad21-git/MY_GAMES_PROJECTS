import random
cnum=random.randint(1,100)
guess=1
while cnum != -1:
    n=int(input("Guess The Number:"))
    if n>cnum:
        print("Lower")
        guess+=1
    elif n<cnum:
        print("Greater")
        guess+=1
    else :
        break
print("BINGO")

print(f"The Number {cnum} you guessed in {guess} attempts")