import random 
number_to_guess=random.randint(1,1000)
guesses=0
while True:
    if guesses==10:
        print("Alas!! you lost the game. you cant guess in 10 attempts")
        break
    answer=int(input("guess the number:"))
    guesses+=1
    if answer==number_to_guess:
        print(f"congrats !! you guessed it right in {guesses} attempts")
        break
    elif answer>number_to_guess:
        print("too high, try again")
    elif answer<number_to_guess:
        print("too low, try again")
