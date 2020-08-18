import json
import random
import requests

def generate_random_word():
    try:
        request = requests.get('https://www.randomlists.com/data/words.json')
        api = json.loads(request.content)
        random_int = random.randint(0,len(api['data']))
        random_word = api['data'][random_int]
        return random_word
    except:
        print('ERROR finding word')

def show_man(tries):
    hang_man = [
    #starting position    
    """
    
     _________           
    |         |
    |
    |
    |
    |
    |
    """,
    #head
    """  
     _________           
    |         |
    |         O 
    |
    |
    |
    |
    
    """,
                
    #head and torso
    """
     _________           
    |         |
    |         O 
    |         |
    |         |
    |
    |
    
    """,
                
    #head,torso and one arm
    """
     _________           
    |         |
    |         O 
    |        \|
    |         | 
    |
    |
    
    """,
        
    #head,torso and both arms
    """
     _________           
    |         |
    |         O 
    |        \|/
    |         | 
    |
    |
    
    """,   
        
    #head,torso,both arms and one leg
    """
     _________           
    |         |
    |         O 
    |        \|/
    |         | 
    |        / 
    |
    
    """,   
        
    #fullbody - game over !
    """
     _________           
    |         |
    |         O 
    |        \|/
    |         | 
    |        / \\
    |
    
    
GAME OVER, COMPUTER WINS !
    """,   
            
    ]
    
    print(hang_man[tries])
   
def play(word):

    #generate the random word to guess by user into a list
    word_as_list = []
    i = iter(word)
    for x in range(0, len(word)):
        word_as_list.append(next(i))
    
    #list of successful user guesses
    word_guess_list = ["_"] *len(word)
    #lists of letters and words guessed
    guessed_letters = []
    guessed_words = []
    
    playing = True
    count = 0
    
    while playing and count < 6:
        show_man(count)
        print('WORD : ' + str(word_guess_list))
        print('\n')
        guess = input('ENTER A LETTER TO GUESS OR THE WORD ITSELF !')
        
        if len(guess) == 1 and guess.lower() in word:
            if guess in guessed_letters:
                print('SORRY YOU HAVE ALREADY GUESSED THIS LETTER')
            else:
                #determine position in word that letter occurs, output will be [character position, character position etc]
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_guess_list[index] = guess
                    guessed_letters.append(guess)
                    if word_guess_list == word_as_list:
                        print('CONGRATULATIONS YOU WIN')
                        playing = False
                    else:
                        continue
        elif len(guess) > 1 and guess.lower() in word:
            if guess in guessed_words:
                print('SORRY YOU HAVE ALREADY GUESSED THIS WORD')
            elif guess == word:
                print('CORRECT WELL DONE')
                playing = False
        else:
            if len(guess) == 1:
                guessed_letters.append(guess)
                print('INCORRECT GUESS !')
                count += 1
                continue
            else:
                guessed_words.append(guess)
                print('INCORRECT GUESS !')
                count += 1
                continue
    if count == 6:
        show_man(count)
      
            
def main():
    word = generate_random_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = generate_random_word()
        play(word)


if __name__ == "__main__":
    main()