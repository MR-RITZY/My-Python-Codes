def GuessTheNumber():
    import random, sys
    choose = random.randint(0,100)
    try:
        guess = input('A number has been choosen by the computer. Can you guess the number right?\n')
        intguess = int(guess)
        while True:
            if intguess > choose:
                print(f'Your guess {guess} too high!\nTry again.')
                guess = input()
                intguess = int(guess)
            elif intguess < choose:
                print(f'Your guess {guess} too low!\nTry again.')
                guess = input()
                intguess = int(guess)
            else:
                print('Wow! You guessed it rights.')
                sys.exit()
    except ValueError:
        while guess == '':
            print("You've not enter any number!")
            GuessTheNumber()
