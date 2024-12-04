def GuessTheNumber():
    import random, sys
    choose = random.randint(0,100)
    try:
        guess = input('A number has been choosen by the computer. Can you guess the number right?\n')
        intguess = int(guess)
        for i in range(3):
            if intguess > choose:
                print(f'Your guess {guess} too high!\nTry again.')
                guess = input()
                intguess = int(guess)
            elif intguess < choose:
                print(f'Your guess {guess} too low!\nTry again.')
                guess = input()
                intguess = int(guess)
            else:
                print('Wow! You guessed it right.')
                sys.exit()
        if intguess != choose:
            print("Time out!\nthe Trial is thrice and you've used it up")
    except ValueError:
        while guess == '':
            print("You've not enter any number!")
            GuessTheNumber()
