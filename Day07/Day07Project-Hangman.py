import random
import Day07HangmanWords
import Day07HangmanArt

chosen_word = random.choice(Day07HangmanWords.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(Day07HangmanArt.logo)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

letter_guessed = []

while not end_of_game:

    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess} ")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        letter_guessed += guess
        print(f"Letters you already tried and aren't in the word: {', '.join(letter_guessed)}")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(Day07HangmanArt.stages[lives])
