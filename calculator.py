import json
import os

# დახმარების ფუნქციები ოპერაციებისათვის
def add(a, b):
    return a + b  # Addition

def subtract(a, b):
    return a - b  # Subtraction 

def multiply(a, b):
    return a * b  # Multiplication 

def divide(a, b):
    if b == 0:  # შემოწმება რიცხვი ნული ხომ არ არის
        raise ValueError("Division by zero is not allowed.")  
    return a / b  # Division 

def floor_divide(a, b):
    if b == 0:  # თუ გამოყოფი ნული იქნება
        raise ValueError("Division by zero is not allowed.")  # დანაყოფი ნულისგან არ შეიძლება
    return a // b  # Floor Division (დაბალ ზღვარზე გაყოფა)

def exponentiate(a, b):
    return a ** b  # Exponentiation 

def calculate_root(a, n):#find root
    if n <= 0:
        print("Root degree must be greater than 0.")
        return None
    return a ** (1 / n)

def calculate_root(a, n):
    if a < 0 and n % 2 == 0:
        print("Cannot calculate an even root of a negative number.")  # ნეგატიური რიცხვის  ფესვის გამოთვლა არ შეიძლება
        return None
    return a ** (1/n)  # Root calculation

# ფაილთან მუშაობა
def save_to_file(filename, data):
    try:
        results = load_from_file(filename)  # სცადე შედეგების წაკითხვა ფაილიდან
    except FileNotFoundError:
        results = []  # თუ ფაილი არ არსებობს, შექმენი ცარიელი სია
    
    results.append(data)  # დაამატე ახალი მონაცემები

    with open(filename, 'w') as file:
        json.dump(results, file, indent=4)  # შეინახე მონაცემები ფაილში JSON ფორმატში

def load_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)  # ჩაწერილი მონაცემების გადმოტანა ფაილიდან

def clear_history(filename):
    if os.path.exists(filename):  # ამოწმებს თუ არსებობს ფაილი
        os.remove(filename)  # შლის ფაილს
# ვალიდაციის შემოწმება
def validate_input(prompt, is_float=False):
    while True:
        user_input = input(prompt).strip()  # მომხმარებლის შეყვანა
        try:
            return float(user_input) if is_float else int(user_input)  # ციფრად კონევრტირება
        except ValueError:
            print("Invalid input. Please enter a number.")  # 

# პროგრამის დაწყება
result = 0  # 
history_file = "calculator_results.json"  # მოქმედებების ისტორია

while True:
    print(f"\n--- Calculator (Current Result: {result}) ---")  #  მიმდინარე შედეგის სტატუსი 
    print("1. Use Current Result ")  # ოპერაციების შესრულება მიმდინარე შედეგით
    print("2. Perform Calculation with Two Numbers ")  # ორი რიცხვის ოპერაციები
    print("3. View History")  # ისტორიის ნახვა
    print("4. Clear Result")  # შედეგის გაწმენდა
    print("5. Clear History")
    print("6. Exit")  # გამოსვლა

    choice = input("Choose an option: ").strip()  # მომხმარებლის არჩევანი

    if choice == "1":  # ოპერაციები მიმდინარე შედეგით
        print("\n--- Operations with Current Result ---")
        print("1. Add (+)")  # დამატება
        print("2. Subtract (-)")  # გამოკლება
        print("3. Multiply (*)")  # გამრავლება
        print("4. Divide (/)")  # გაყოფა
        print("5. Floor Division (//)")  # 0.1// გაყოფა
        print("6. Exponentiate (**)")  # ახარისხება
        print("7. find root(**1/n)") #ფესვის პოვნა
        operation = validate_input("Choose an operation: ")  # მომხმარებელს სთხოვს, აირჩიოს ოპერაცია

        operand = input("Enter a number or type 'result' to use the current result: ").strip().lower()  # operand-ის შეყვანა
        if operand == 'result':
            operand = result  # თუ operand არის "result", გამოიყენე მიმდინარე შედეგი
        else:
            operand = validate_input("Enter a valid number: ", is_float=True)  # რიცხვის ვალიდაცია

        try:
            if operation == 1:
                result = add(result, operand)
            elif operation == 2:
                result = subtract(result, operand)
            elif operation == 3:
                result = multiply(result, operand)
            elif operation == 4:
                result = divide(result, operand)
            elif operation == 5:
                result = floor_divide(result, operand)
            elif operation == 6:
                result = exponentiate(result, operand)
            elif operation == 7:
                result = calculate_root(result, operand)
            else:
                print("Invalid operation selected.")  # არასწორი ოპერაცია
                continue

            print(f"Result: {result}")  # შედეგის გამოჩენა
            save_to_file(history_file, f"result {['+', '-', '*', '/', '//', '**'][operation - 1]} {operand} = {result}")
        except ValueError as e:
            print(f"Error: {e}")  # შეცდომის გამოტანა

    elif choice == "2":  # ორი რიცხვის ოპერაციები
        print("\n--- Operations with Two Numbers ---")
        num1 = validate_input("Enter the first number: ", is_float=True)  # პირველი რიცხვის შეყვანა
        print("Supported operations: +, -, *, /, //, **,**1/n")  # შესაძლო ოპერაციები
        operator = input("Enter the operator: ").strip()  # ოპერატორის შეყვანა
        num2 = validate_input("Enter the second number: ", is_float=True)  # მეორე რიცხვის შეყვანა

        try:
            if operator == "+":
                result = add(num1, num2)
            elif operator == "-":
                result = subtract(num1, num2)
            elif operator == "*":
                result = multiply(num1, num2)
            elif operator == "/":
                result = divide(num1, num2)
            elif operator == "//":
                result = floor_divide(num1, num2)
            elif operator == "**":
                result = exponentiate(num1, num2)
            elif operator == "**1/n":
                result = calculate_root(num1, num2)
            else:
                print("Invalid operator.")  # არასწორი ოპერატორი
                continue

            print(f"Result: {result}")  # შედეგის გამოჩენა
            save_to_file(history_file, f"{num1} {operator} {num2} = {result}")
        except ValueError as e:
            print(f"Error: {e}")  # შეცდომა

    elif choice == "3":  # ისტორიის ნახვა
        print("\n--- Calculation History ---")
        try:
            history = load_from_file(history_file)  # შედეგების ისტორიის წაკითხვა
            if history:
                for res in history:
                    print(res)  # ყველა ისტორიის ჩანაწერის ჩვენება
            else:
                print("No history available.")  # თუ ისტორია ცარიელია
        except FileNotFoundError:
            print("No history available.")  # თუ ისტორია არ არსებობს

    elif choice == "4":  # შედეგის გაწმენდა
        result = 0  # 
        print("Result cleared. Reset to 0.")  # შეტყობინება

    elif choice == "5":
        clear_history(history_file)  # შლის მთლიან მეხსიერებას
        print("History cleared.")

    elif choice == "6":  # გამოსვლა
        print("Exiting the calculator. Goodbye!")  # გამოსვლა
        break

    else:
        print("Invalid choice. Please select a valid option.")  # შეცდომა არჩევისას
