import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")  # თამაშის დაწყების შეტყობინება
    print("You can type 'exit' at any time to quit the game.")  # მოთამაშეს შეუძლია შეიყვანოს 'exit', რათა გააჩეროს თამაში

    print("Choose a difficulty level:")  # სირთულის დონეს არჩევა
    print("1. Easy (Range: 1-50, Attempts: 15)")  # მარტივი დონე
    print("2. Medium (Range: 1-100, Attempts: 10)")  # საშუალო დონე
    print("3. Hard (Range: 1-200, Attempts: 5)")  # რთული დონე
    print("4. Custom (Choose your own range and attempts)")  # მომხმარებლისთვის საკუთარი შეზღუდვების არჩევა

    # მომხმარებლის არჩევანის მიღება
    while True:
        choice = input("Enter 1, 2, 3, or 4: ")  # მომხმარებელს სთხოვს, აირჩიოს სირთულის დონე
        if choice == '1':
            lower, upper, max_attempts = 1, 50, 15  # მარტივი დონე
            break
        elif choice == '2':
            lower, upper, max_attempts = 1, 100, 10  # საშუალო დონე
            break
        elif choice == '3':
            lower, upper, max_attempts = 1, 200, 5  # რთული დონე
            break
        elif choice == '4':
            # მომხმარებელს სთხოვს, შეიყვანოს საკუთარი დიაპაზონი და მაქსიმალური მცდელობები
            lower = int(input("Enter the lower bound: "))  
            upper = int(input("Enter the upper bound: "))  
            max_attempts = int(input("Enter the maximum number of attempts: "))
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")  # არასწორი არჩევანი

    # შემთხვევითი ნომრის შერჩევა არსებული დიაპაზონის მიხედვით
    random_number = random.randint(lower, upper)  
    attempts = 0  # მცდელობების რაოდენობა

    print(f"\nI've picked a number between {lower} and {upper}. Can you guess it?")  # ტერმინალის შეტყობინება
    print(f"You have {max_attempts} attempts to guess the number.\n")  # მცდელობების მაქსიმალური რაოდენობა

    # ითვლის მცდელობების რაოდენობას, სანამ მომხმარებელი სწორ პასუხს არ გასცემს ან მცდელობები არ ამოიწურება
    while attempts < max_attempts:
        user_input = input("Enter your guess: ")  # მომხმარებელს სთხოვს, შეიტანოს თავის ვარაუდი

        if user_input.lower() == 'exit':  # თუ მომხმარებელი დაწერს 'exit', თამაში წყდება
            print("Thanks for playing! Goodbye!")
            break

        try:
            guess = int(user_input)  # მომხმარებლის ვარაუდი ციფრად
        except ValueError:
            print("Please enter a valid number.")  # არასწორი პასუხი
            continue

        attempts += 1  # მცდელობების რაოდენობის გაზრდა

        if guess < random_number:
            print("Too low! Try again.")  # ძალიან დაბალი ვარაუდი
        elif guess > random_number:
            print("Too high! Try again.")  # ძალიან მაღალი ვარაუდი
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")  # სწორი პასუხი
            break
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {random_number}. Better luck next time!")  # თუ მცდელობების რაოდენება ამოიწურა,რომ აცნობოს მომხმარებელს

guess_the_number()  # თამაშის დაწყება
