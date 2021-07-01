"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random
def super_asker(low, high, message):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    Try to call at least one of the other functions to minimise the
    amount of code.
    """
    while True:
        try:
            ask_for_number = input(message)
            print(ask_for_number, "here")
            ask_for_number = int(ask_for_number)
            print("{} is a number".format(ask_for_number))
            if low < ask_for_number < high:
                print("Well done, {} is within range".format(ask_for_number))
                return ask_for_number
        except Exception as e:
            print(f"{e} is not a number **")
        


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    
    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")

    lowerBound = super_asker(-1000, 1000, "Enter a lower bound:")
    upperBound = super_asker(lowerBound, 1000, "Enter an upper bound: ")


    actualNumber = random.randint(lowerBound, upperBound)

    while True:
      guessedNumber = super_asker(lowerBound, upperBound, f"Guess a number between {lowerBound} and {upperBound}: ")
      print("You guessed {},".format(guessedNumber))
      if guessedNumber == actualNumber:
        print("You guessed it!! It was {}".format(actualNumber))
        return "You got it!"
      elif guessedNumber < actualNumber:
        print("Too small, try again :'(")
      else:
        print("Too big, try again :'(")
     
    
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
