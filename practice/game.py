import random
# Start the game loop
play__again = "yes"

while play__again.lower() == "yes":
    secret_number = random.randint(1, 10)
    guess_count = 0 #Initialize  guess count
    while True:
       guess = int(input("guess a number: "))
       guess_count += 1 #Increment after each guesst

    match guess:
          case _ if guess == secret_number:
            print("Congratulations, you guessed it!")
          case _ if guess > secret_number:
            print("Oops, your guess is a bit high. Try again!")
          case _ if guess < secret_number:
            print("Nope, your guess is a bit low. Give it another shot!")
    
    play__again = input("Would you like to play again? (yes or no): ")

print("Game Over!")


    


    
