import json  # JSON module for data management

# წიგნის კლასის განმარტება
class Book:
    # კლასი აღწერს წიგნს სათაურით, ავტორითა და გამოცემის წელი.
    def __init__(self, title, author, year):
        self.title = title  # წიგნის სათაური
        self.author = author  # ავტორი
        self.year = year  # გამოცემის წელი

    def __str__(self):
        return f"'{self.title}' by {self.author}, published in {self.year}"

# წიგნების მენეჯმენტის კლასის განმარტება
class BookManager:
    # კლასი, რომელიც პასუხისმგებელია წიგნების კოლექციის მართვაზე, მათ შორის დამატებაზე,გამოტანასა  და ძიებაზე.
    def __init__(self, filename="books.json"):
        self.filename = filename  # JSON ფაილის სახელი
        self.books = self.load_books()  # წიგნების მონაცემთა ჩატვირთვა

    def load_books(self):
        # მონაცემების ჩატვირთვა JSON ფაილიდან
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)  # JSON-ის მონაცემების წაკითხვა
                return [Book(**book) for book in data]  # მონაცემთა კონვერტაცია Book ობიექტებად
        except FileNotFoundError:
            # თუ ფაილი არ არსებობს, დაბრუნდება ცარიელი სია
            return []

    def save_books(self):
        # მონაცემების შენახვა JSON ფაილში
        with open(self.filename, "w") as file:
            data = [book.__dict__ for book in self.books]  # Book ობიექტების ლექსიკონებად გადაყვანა
            json.dump(data, file, indent=4)  # მონაცემების ფორმატირებული ჩაწერა JSON-ში

    def add_book(self, title, author, year):
        # ამატებს ახალ წიგნს კოლექციაში, თუ ის უკვე არ არსებობს
        if not any(b.title.lower() == title.lower() and b.author.lower() == author.lower() for b in self.books):
            new_book = Book(title, author, year)
            self.books.append(new_book)  # წიგნის დამატება სიაში
            self.save_books()  # ცვლილებების შენახვა JSON ფაილში
            print(f"Book '{title}' by {author} has been successfully added!")
        else:
            print(f"Book '{title}' by {author} already exists in the collection.")

    def view_books(self):
        # გამოაქვს მთლიანი ინფორმაცია
        if self.books:
            print("\nBook list:")
            for book in self.books:
                print(book)  #
        else:
            print("No books available in the collection.")

    def search_by_title(self, title):
        # ეძებს წიგნს სათაურის მიხედვით
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_author(self, author):
        # ეძებს წიგნს ავტორის მიხედვით
        return [b for b in self.books if author.lower() in b.author.lower()]

    def search_by_year(self, year):
        # ეძებს წიგნს გამოშვების წლის მიხედვით
        return [b for b in self.books if b.year == str(year)]

# ვალიდაციის ფუნქციები
def validate_year(year):
    # ამოწმებს წლის ვალიდურობას
    if year.isdigit() and int(year) > 0:
        return int(year)  # ვალიდური წელი
    else:
        print("Invalid year! Please enter a valid positive year.")
        return None

def validate_non_empty(input_string):
    # ამოწმებს რომ შეყვანილი ინფორმაცია ცარიელი არ იყოს
    if input_string.strip():
        return input_string.strip()  
    else:
        print("Input cannot be empty! Please enter valid data.")
        return None

# მთავარი ფუნქცია
def main():
    manager = BookManager()  # წიგნების მენეჯერის ობიექტის შექმნა

    # მაგალითების დამატება კოლექციაში
    example_books = [
        ("To Kill a Mockingbird", "Harper Lee", 1960),
        ("1984", "George Orwell", 1949),
        ("Pride and Prejudice", "Jane Austen", 1813),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925),
        ("Moby-Dick", "Herman Melville", 1851),
    ]
    for title, author, year in example_books:
        manager.add_book(title, author, year)  

    while True:
        # მენიუს გამოტანა ეკრანზე
        print("\nMenu:")
        print("1. Add a Book")  # წიგნის დამატება
        print("2. View All Books")  # ყველა წიგნის ნახვა
        print("3. Search Book by Title")  # ძიება სათაურით
        print("4. Search Book by Author")  # ძიება ავტორით
        print("5. Search Book by Year")  # ძიება გამოშვების წლით
        print("6. Exit")  # პროგრამის დასრულება

        choice = input("Enter your choice (1-6): ")  # მომხმარებლის არჩევანის შეყვანა

        if choice == '1':
            # მონაცემების ინიცირება
            title = author = year = None

            # წიგნის სათაურის შეყვანა
            while title is None:
                title = validate_non_empty(input("Enter the book title: "))  # ვალიდაციის შემოწმება

            # ავტორის სახელის შეყვანა
            while author is None:
                author = validate_non_empty(input("Enter the author's name: "))  # ვალიდაციის შემოწმება

            # გამოცემის წლის შეყვანა
            while year is None:
                year = validate_year(input("Enter the publication year: "))  # ვალიდაციის შემოწმება

            # ახალი წიგნის დამატება
            manager.add_book(title, author, year)

        elif choice == '2':
            # მთლიანი ინფორმაციის გამოტანა
            manager.view_books()

        elif choice == '3':
            # ძიება სათაურის მიხედვით
            search_title = input("Enter the book title to search for: ")
            results = manager.search_by_title(search_title)
            if results:
                print("\nSearch results:")
                for book in results:
                    print(book)  # ნაპოვნი წიგნების ჩვენება
            else:
                print(f"No books found with the title '{search_title}'.")

        elif choice == '4':
            # ძიება ავტორის მიხედვით
            search_author = input("Enter the author's name to search for: ")
            results = manager.search_by_author(search_author)
            if results:
                print("\nSearch results:")
                for book in results:
                    print(book)  # ნაპოვნი წიგნების ჩვენება
            else:
                print(f"No books found by author '{search_author}'.")

        elif choice == '5':
            # ძიება წლის მიხედვით
            search_year = input("Enter the year to search for: ")
            results = manager.search_by_year(search_year)
            if results:
                print("\nSearch results:")
                for book in results:
                    print(book)  # ნაპოვნი წიგნების ჩვენება
            else:
                print(f"No books found published in {search_year}.")

        elif choice == '6':
            # პროგრამის დასრულება
            print("Exiting the program. Goodbye!")
            break

        else:
            # არასწორი არჩევანის შეტყობინება
            print("Invalid choice. Please enter a number between 1 and 6.")

