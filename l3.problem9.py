# L3 Problem 9

low = 0
high = 100
guess = (low + high) / 2

print "Please think of a number between " + str(low) + " and " + str(high) + "!"

while True:
    print("Is your secret number " + str(guess) + "?")
    print "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.",
    answer = raw_input("Enter 'c' to indicate I guessed correctly. ")

    if answer == 'h':
        high = guess
        guess = (low + high) / 2
    elif answer == 'l':
        low = guess
        guess = (low + high) / 2
    elif answer == 'c':
        print("Game over. Your secret number was: " + str(guess))
        break
    else:
        print("Invalid Answer! Please enter 'h', 'l', or 'c'.")
