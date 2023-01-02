from words import word_list
import random
def get_word(words):
    word = random.choice(words)
    return word.lower()


#Choosing a word

chosen_word = get_word(word_list)

#Printing blanks of words

def underscore_word():
    hidden_word = []    
    for n in range(len(chosen_word)):
        hidden_word.append("_")
    return hidden_word
hidden_list = underscore_word()
print(hidden_list)

#hangman ascii

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print("""_                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
""")

#rmb to make sure only 1 letter
#check if guess is correct and keeping track of life

game_run = True
life = 0
list = []
while game_run == True:
    guess = input("Guess a letter: ").lower()
    if guess in list:
        print("You have already guessed this letter")
        continue
    list.append(guess)
    count = 0
    correct = False
    for letter in chosen_word:
        if letter == guess:
            #print("Right")
            hidden_list[count] = guess
            count += 1
            correct = True
               
        else:
            #print("Wrong")
            count += 1
            
    if correct == False:
        print(HANGMANPICS[life])
        life += 1
        if life == 7:
            print("You lose!")
    elif correct == True:
        print(HANGMANPICS[life])

    print(hidden_list)
    if "_" not in hidden_list:
        game_run = False
        print("You win!")

print(chosen_word)
#modify underscore

