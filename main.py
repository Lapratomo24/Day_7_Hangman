import random
from hangman_ascii import logo, stages
from hangman_words import word_list

selected_word = random.choice(word_list)
word_length = len(selected_word)

game_over = False

lives = 6

# game logic

print(logo)
print("")
print("Guess the correct letters!")

display = []

for _ in range(word_length):
    display += "_"
    
while not game_over:
    guess = input("Your letter: ").lower()
    print("")
    
    if guess in display:
        print("You've already guessed this letter. Try again.")
        print("")
    
    for position in range(word_length):
        letter = selected_word[position]
        
        if letter == guess:
            display[position] = letter
    
    if guess not in selected_word:
        print(f"The word does not contain the letter {guess}.")
        print("")
        lives -= 1
        
        if lives == 0:
            game_over = True
            print("You lose!")
            print("")
            print(f"The word you're looking for is {selected_word}.")
            print("")
    
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        game_over = True
        print("You win!")
        print("")

    print(stages[lives])
    print("")