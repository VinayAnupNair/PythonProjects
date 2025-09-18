import random

num = random.randint(1,100)
correct = False
tries = 0
while(not correct):
    guess = int(input("What do you guess(from 0 to 100): "))
    if guess > num:
        print("Too High")
    elif guess < num:
        print("Too Low")
    else:
        print("You got it!")
        correct = True
    tries+=1
print(f"you got it in {tries} tries")
print("End")