import random

def choose_word():   #firstly choose a word
    words = ['python', 'java', 'hangman', 'computer', 'programming', 'developer','laptop']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    word = choose_word()   #choose word store in  word
    guessed_letters = set() #store guessed letters
    incorrect_guesses = 0
    max_attempts = 6
    
    print("------------Welcome to Hangman!-------------")
    
    while incorrect_guesses < max_attempts:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess not in word:
            incorrect_guesses += 1
            remaining_guesses=max_attempts-incorrect_guesses
            print(f"Incorrect guess! You have {remaining_guesses} attempts left.")
        
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            return
    
    print("\nGame over! The word was:", word)

if __name__ == "__main__":
    hangman()
