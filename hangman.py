import random

def select_random_word():
    words = ["apple", "banana", "orange", "grape", "cherry", "pineapple", "watermelon", "strawberry", "mango"]
    return random.choice(words)

def display_word(select_word,user_input):
    #firstly,   (random_word aauxa,empty)
    display = ""
    for letter in select_word:
       
        # It will convert into underscore.
        
        if letter in user_input:
            #Because of empty it will go into else condition. 
            display += letter
            # if guess word is corect, it will replace underscore of that place.
        else:
            display += "_"
    return display
# return underscore in the first step based on how many letter does a random choice have.

def hangman_game():
    print("Welcome to Hangman!")
    print("Try to guess the word one letter at a time. You have 6 attempts.")

    select= select_random_word()
    letter=set()
    attempts = 6

    while True:
        print("\n"+display_word(select,letter))
        #helps to get underscore in first step of program.

        if "_" not in display_word(select,letter):
            #if there is no underscore in display, it will print the below statement.
            print("Congratulations! You guessed the word:", select)
            break

        if attempts == 0:
            #if one cannot guess it.
            print("Sorry, you ran out of attempts. The word was:", select)
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            #length should be 1 and it should be alphabet otherwise it will be continue from beginning.
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in letter:
            # if the character is repeated then it will continue from beginning.
            print("You've already guessed that letter.")
            continue

        letter.add(guess)
        #if it passes above 2 mention if statement, it will be added onto letter variable.
        
        

        if guess not in select:
            #To count the attempt if the guessed letter is not in random selected word.
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

if __name__ == "__main__":
    hangman_game()
    # to call function.
    