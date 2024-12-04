import random

# სიტყვების სია სხვადასხვა სირთულის დონის მიხედვით შედგენილი. მარტივი დონეზე მოკლე სიტყვები შემდეგ რთულდება.
easy_words = ["ნინო", "გიორგი", "მარიამი", "ლუკა", "ანო"]
medium_words = ["გივი", "თამარ", "ანასტასია", "სანდრო", "ნატალია"]
hard_words = ["ვახტანგი", "თეოდორა", "ზაქარია", "ლევანი", "ეკატერინე"]

def hangman():
    print("Welcome to Hangman!")
    print("You can type 'exit' at any time to quit the game.")
    
    # სირთულის დონის არჩევა
    print("\nChoose a difficulty level:")
    print("1. Easy (Short words)")
    print("2. Medium (Moderate length words)")
    print("3. Hard (Longer words)")
    
    level = input("Choose a level (1, 2, or 3): ").strip()
    
    # სირთულის დონე
    if level == "1":
        words = easy_words  # მარტივი დონე
    elif level == "2":
        words = medium_words  # საშუალო დონე
    elif level == "3":
        words = hard_words  # რთული დონე
    else:
        print("Invalid choice. Defaulting to Medium level.")
        words = medium_words

    # მცდელობების რაოდენობის არჩევა
    while True:
        try:
            attempts = int(input("\nEnter the number of attempts you'd like to have: ").strip())
            if attempts <= 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # შემთხვევით ირჩევა სიტყვა შესაბამისი სირთულის მიხედვით
    word = random.choice(words).lower()
    word_length = len(word)
    guessed_letters = []  # გამოცნობილი ასოები
    word_guessed = ['_'] * word_length  # სიტყვების აღწერა _ სიმობლოთი

    print(f"\nI've chosen a word. It has {word_length} letters.")
    print(f"You have {attempts} attempts to guess the word.")

    while attempts > 0:
        print("\nWord:", ' '.join(word_guessed))
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        guess = input("Enter a letter or guess the whole word: ").lower()

        # თამაშის დასრულება
        if guess == "exit":
            print("Thanks for playing! Goodbye!")
            break

        # თუ მოთამაშემ სცადა მთელი სიტყვის გამოცნობა
        if len(guess) > 1:
            if guess == word:
                print(f"Congratulations! You've guessed the word: {word.title()}")
                break
            else:
                print(f"Wrong guess! The word was '{word.title()}'. Game Over.")
                break

        # ამოწმებს შეტანილის სიმბოლოს ვალიდურობას
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue
        
        # ამოწმებს უკვე იქნა თუ არა რომ ეს ასო უკვე იქნა თუ არა გამოყენებული
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
        
        # ამატებს გამოცნობილ ასოებს
        guessed_letters.append(guess)

        # ამოწმეს შეტანილი ასო გვხდება თუ არა სიტყვაში
        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
            
            # გამოაქვს გამოცნობილი ასოები
            for i in range(word_length):
                if word[i] == guess:
                    word_guessed[i] = guess
            
            # ამოწმებს გამოიცნო თუ არა მომხმარებელმა სიტყვა
            if ''.join(word_guessed) == word:
                print(f"Congratulations! You've guessed the word: {word.title()}")
                break
        else:
            print(f"Oops! The letter '{guess}' is not in the word.")
            attempts -= 1

    # თუ მცდელობები ამოიწურა, თამაში მთავრდება
    if attempts == 0:
        print(f"Sorry, you've run out of attempts! The word was '{word.title()}'.")

# თამაშის დაწყება
hangman()
