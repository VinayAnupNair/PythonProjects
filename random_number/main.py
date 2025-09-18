# this line is used so that we can use the random module
import random

# declaring a number which is randomly assigned from the range to 100
num = random.randint(1,100)
tries = 0

# starting the loop
while(True):

    # try catch block to ensure that valid inputs are recieved
    try:

        # taking the input from the console
        guess = int(input("What do you guess(from 1 to 100): "))

        # checking if guess is within the bounds, if not we loop back until it is
        if guess > 100:
            print("That's impossible too high enter again")
            continue
        if guess < 1:
            print("That's impossible too low enter again")
            continue
    
    #checking if i value other than integer is entered
    except ValueError:
        print("Please enter an integer only")
        continue

    # giving clues to the user    
    if guess > num:
        print("Too High")
    elif guess < num:
        print("Too Low")
    else:

        # success message
        print(f"you got it in {tries} tries")
        break