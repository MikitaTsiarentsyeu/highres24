class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__available = True  # Приватное поле доступности

    def check_out(self):
        if self.__available:
            self.__available = False
            print(f"'{self.title}' has been checked out.")
        else:
            print(f"Sorry, '{self.title}' is currently not available.")

    def return_book(self):
        if not self.__available:
            self.__available = True
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not checked out.")

    def get_book_info(self):
        status = "Available" if self.__available else "Checked out"
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nStatus: {status}"

book1 = Book("dfb", "djlslnl jdkj", "978-0451524935")
book2 = Book("human", "murakami", "978-0060935467")

print(book1.get_book_info())
print()

book1.check_out()

print()
print(book1.get_book_info())
print()

book1.return_book()

print()
print(book1.get_book_info())
print()

print(book2.get_book_info())
book2.check_out()
print(book2.get_book_info())