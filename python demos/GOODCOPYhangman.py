import random
from this import d
# i didnt use a separate folder for the list
words = ['kwantlen', 'rai', 'zimmerman', 'drain gang', 'amygdala', 'awesomeness', 'deoxyribonucleicacid', 'freddyfazbear', 'tacobell',\
    'bladee', 'icecream', 'pizza', 'axolotl', 'lizard', 'simulation', 'valorant', 'kanye', 'cinnamon', 'shakespeare', 'californiaroll']
from hangman_visual import lives_visual_dict
import string 

import time


def choose_valid_word(words): #function chooses a random word from the list
    word = random.choice(words)
    while 'kwantlen' in word or 'rai' in word or 'zimmerman' in word: #skips 'kwantlen', 'rai', & 'zimmerman'
        word = random.choice(words)

    return word.upper()

def hangman(): 
    word = choose_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase) 
    used_letters = set() 

    lives = 7

    #getting user input 
    while len(word_letters) > 0 and lives  > 0:
        # letters used 
        print('You have', lives, 'lives left and you  have used these letters: ', ''.join(used_letters))

        # what the current word is with dashes (W - R D)
        wordlist = [letter if letter in used_letters else "-" for letter in word]
        time.sleep(1)
        print(lives_visual_dict[lives])
        print('Current word: ', ''.join(wordlist))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            nice_comment = ['so awesome', 'legendary', 'you are a pro'] #randomly selects a nice comment if guess is correct
            comment = random.choice(nice_comment)
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 # takes away a life if guess is incorrect
                print('That letter is not in the word.')
                mean_comment = ['so bad..', 'do better lol', 'get good', ]
                comment = random.choice(mean_comment) #randomly selects a mean comment if guess is wrong
                print(comment)

        elif user_letter in used_letters:
            print('Character already guessed. Try again. ')
        else:
            print('Invalid character. Try again' )

# gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print ('YOU DIED. NO LIVES LEFT. The word was', word)
    else:
        print('You guessed the word', word, 'correctly!')


hangman()

if __name__ == '__main__':
    while True: # asks player if they want to  play again. IF yes, runs again, if no, then game exits
        again = str(input("Do you want to play again (type yes or no): "))
        if again == "yes":
                hangman()
        elif again == "no":
            print("game done")
            break
